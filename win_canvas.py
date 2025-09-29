# app/win_canvas.py
import tkinter as tk
from tkinter import ttk

def open_win_canvas(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Panel de Ajustes")
    win.geometry("480x360")
    win.minsize(400, 300)

    # --- Encabezado ---
    header = ttk.Frame(win)
    header.pack(fill="x", padx=8, pady=8)

    ttk.Label(header, text="Ajustes", font=("Segoe UI", 14, "bold")).pack(side="left")
    ttk.Button(header, text="✕", width=3, command=win.destroy).pack(side="right")

    # --- Contenido principal ---
    content = ttk.Frame(win, padding=12)
    content.pack(fill="both", expand=True)

    left = ttk.Frame(content)
    left.pack(side="left", fill="both", expand=True)

    right = ttk.Frame(content, width=160)
    right.pack(side="right", fill="y")

    # Variables
    vol_var = tk.DoubleVar(value=50)
    brig_var = tk.DoubleVar(value=70)
    contraste_var = tk.DoubleVar(value=50)

    def make_slider(parent, text, var, frm=0, to=100, step=1):
        frm_cont = ttk.Frame(parent)
        frm_cont.pack(fill="x", pady=6)

        ttk.Label(frm_cont, text=text).pack(anchor="w")
        # Usamos command para actualizar la etiqueta en tiempo real
        lbl_value = ttk.Label(frm_cont, text=f"{var.get():.0f}")
        def on_move(val):
            try:
                v = float(val)
            except Exception:
                v = var.get()
            var.set(v)
            lbl_value.config(text=f"{v:.0f}")

        scale = ttk.Scale(frm_cont, from_=frm, to=to, orient="horizontal",
                          command=on_move)
        scale.set(var.get())
        scale.pack(fill="x")
        lbl_value.pack(anchor="e")

        # También intentamos enlazar trace (compatibilidad con distintas versiones)
        def trace_update(*_):
            lbl_value.config(text=f"{var.get():.0f}")
        try:
            # Python >= 3.6
            var.trace_add("write", lambda *a: trace_update())
        except AttributeError:
            # Fallback más antiguo
            try:
                var.trace("w", lambda *a: trace_update())
            except Exception:
                pass

        return scale

    make_slider(left, "Volumen", vol_var, 0, 100)
    make_slider(left, "Brillo", brig_var, 0, 100)
    make_slider(left, "Resolucion", contraste_var, 0, 100)

    # Opciones a la derecha
    ttk.Label(right, text="Opciones").pack(anchor="nw", pady=(0,6))

    modo_noche = tk.BooleanVar(value=False)
    ttk.Checkbutton(right, text="Modo nocturno", variable=modo_noche).pack(anchor="nw", pady=4)

    notif_var = tk.BooleanVar(value=True)
    ttk.Checkbutton(right, text="Notificaciones", variable=notif_var).pack(anchor="nw", pady=4)

    # Pequeño canvas de vista previa en el panel derecho
    canvas = tk.Canvas(right, width=140, height=100, bg="white", highlightthickness=1, highlightbackground="#ccc")
    canvas.pack(pady=10)
    canvas.create_rectangle(10, 10, 60, 40, outline="black", width=2)
    canvas.create_oval(70, 10, 120, 40, fill="lightblue")
    canvas.create_text(70, 70, text="Preview", font=("Segoe UI", 8, "bold"))

    def restore_defaults():
        vol_var.set(50)
        brig_var.set(70)
        contraste_var.set(50)
        modo_noche.set(False)
        notif_var.set(True)

    ttk.Button(right, text="Restaurar valores", command=restore_defaults).pack(anchor="s", pady=12, side="bottom")

    # --- Barra inferior ---
    bottom = ttk.Frame(win)
    bottom.pack(fill="x", padx=8, pady=8)

    status_var = tk.StringVar(value="Listo")

    def save_settings():
        ajustes = {
            "volumen": vol_var.get(),
            "brillo": brig_var.get(),
            "contraste": contraste_var.get(),
            "modo_noche": modo_noche.get(),
            "notificaciones": notif_var.get(),
        }
        print("Ajustes guardados:", ajustes)
        status_var.set("Guardado")

    ttk.Button(bottom, text="Guardar", command=save_settings).pack(side="right")
    ttk.Label(bottom, textvariable=status_var).pack(side="left")

    # Atajos
    def _save_bind(e): 
        save_settings()
    win.bind('<Control-s>', _save_bind)
    win.bind('<Escape>', lambda e: win.destroy())
