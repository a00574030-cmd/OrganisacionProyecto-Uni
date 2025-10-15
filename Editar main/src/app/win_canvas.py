import tkinter as tk
from tkinter import ttk

# 🔑 Añadimos apply_settings_callback
def open_win_canvas(parent: tk.Tk, apply_settings_callback=None):
    win = tk.Toplevel(parent)
    win.title("⚙️ Panel de Ajustes Avanzados")
    win.geometry("580x480")
    win.minsize(500, 400)
    win.configure(bg='#f8f9fa')

    # Colores para la interfaz
    COLORS = {
        "primary": "#4a90e2",
        "success": "#48bb78",
        "warning": "#ed8936",
        "danger": "#f56565",
        "dark": "#2d3748",
        "light": "#f8f9fa",
        "gray": "#e2e8f0"
    }

    # --- Encabezado Mejorado ---
    header = tk.Frame(win, bg=COLORS["primary"], height=60)
    header.pack(fill="x", padx=0, pady=0)
    
    header_content = tk.Frame(header, bg=COLORS["primary"])
    header_content.pack(fill="both", padx=16, pady=12)
    
    tk.Label(header_content, text="⚙️ PANEL DE AJUSTES", 
             font=("Segoe UI", 16, "bold"), 
             bg=COLORS["primary"], 
             fg="white").pack(side="left")
    
    # Botón cerrar con mejor estilo
    close_btn = tk.Button(header_content, text="✕", 
                         font=("Segoe UI", 12, "bold"),
                         bg=COLORS["primary"],
                         fg="white",
                         relief="flat",
                         bd=0,
                         width=3,
                         cursor="hand2",
                         command=win.destroy)
    close_btn.pack(side="right")
    
    # Efecto hover para botón cerrar
    close_btn.bind("<Enter>", lambda e: close_btn.config(bg="#357abd"))
    close_btn.bind("<Leave>", lambda e: close_btn.config(bg=COLORS["primary"]))

    # --- Contenido principal ---
    main_container = tk.Frame(win, bg='#f8f9fa')
    main_container.pack(fill="both", expand=True, padx=16, pady=16)

    # Panel izquierdo - Controles
    left_panel = tk.Frame(main_container, bg='#f8f9fa')
    left_panel.pack(side="left", fill="both", expand=True, padx=(0, 16))

    # Panel derecho - Vista previa y opciones
    right_panel = tk.LabelFrame(main_container, text="🎯 Vista Previa & Opciones", 
                               font=("Segoe UI", 10, "bold"),
                               bg='#f8f9fa',
                               fg=COLORS["dark"],
                               padx=12,
                               pady=12,
                               width=200)
    right_panel.pack(side="right", fill="y")
    right_panel.pack_propagate(False)

    # Variables
    vol_var = tk.DoubleVar(value=50)
    brig_var = tk.DoubleVar(value=70)
    resolucion_var = tk.DoubleVar(value=50)

    # Función mejorada para crear sliders
    def create_modern_slider(parent, text, var, icon, color, frm=0, to=100, step=1):
        frame = tk.Frame(parent, bg='#f8f9fa')
        frame.pack(fill="x", pady=10)
        
        # Header del slider
        header_frame = tk.Frame(frame, bg='#f8f9fa')
        header_frame.pack(fill="x", pady=(0, 8))
        
        tk.Label(header_frame, text=f"{icon} {text}", 
                font=("Segoe UI", 11, "bold"),
                bg='#f8f9fa',
                fg=COLORS["dark"]).pack(side="left")
        
        value_label = tk.Label(header_frame, text=f"{var.get():.0f}%",
                             font=("Segoe UI", 10, "bold"),
                             bg='#f8f9fa',
                             fg=color)
        value_label.pack(side="right")
        
        # Slider con estilo personalizado
        def on_slider_move(val):
            try:
                v = float(val)
                var.set(v)
                value_label.config(text=f"{v:.0f}%")
                update_preview()
            except ValueError:
                pass
        
        slider = tk.Scale(frame, from_=frm, to=to, orient="horizontal",
                         variable=var,
                         command=on_slider_move,
                         length=250,
                         sliderrelief="flat",
                         troughcolor=COLORS["gray"],
                         activebackground=color,
                         bg='#f8f9fa',
                         fg=COLORS["dark"],
                         highlightbackground=COLORS["gray"],
                         borderwidth=1,
                         relief="sunken")
        slider.pack(fill="x")
        
        # Marcas de referencia
        marks_frame = tk.Frame(frame, bg='#f8f9fa')
        marks_frame.pack(fill="x")
        
        tk.Label(marks_frame, text=f"{frm}", font=("Segoe UI", 7), bg='#f8f9fa', fg=COLORS["dark"]).pack(side="left")
        tk.Label(marks_frame, text=f"{to}", font=("Segoe UI", 7), bg='#f8f9fa', fg=COLORS["dark"]).pack(side="right")
        
        return slider

    # Crear sliders con estilo moderno
    create_modern_slider(left_panel, "Volumen", vol_var, "🔊", COLORS["primary"])
    create_modern_slider(left_panel, "Brillo", brig_var, "💡", COLORS["warning"])
    create_modern_slider(left_panel, "Resolución", resolucion_var, "🖥️", COLORS["success"])

    # Opciones en el panel derecho
    options_frame = tk.Frame(right_panel, bg='#f8f9fa')
    options_frame.pack(fill="x", pady=(0, 15))

    tk.Label(options_frame, text="Configuración:", 
             font=("Segoe UI", 11, "bold"),
             bg='#f8f9fa',
             fg=COLORS["dark"]).pack(anchor="w", pady=(0, 8))

    modo_noche = tk.BooleanVar(value=False)
    notif_var = tk.BooleanVar(value=True)
    auto_save_var = tk.BooleanVar(value=True)

    def create_checkbutton(parent, text, var, icon):
        btn = tk.Checkbutton(parent, 
                           text=f"{icon} {text}",
                           variable=var,
                           font=("Segoe UI", 10),
                           bg='#f8f9fa',
                           fg=COLORS["dark"],
                           activebackground='#f8f9fa',
                           activeforeground=COLORS["dark"],
                           selectcolor=COLORS["primary"],
                           command=update_preview)
        btn.pack(anchor="w", pady=6)
        return btn

    create_checkbutton(options_frame, "Modo Nocturno", modo_noche, "🌙")
    create_checkbutton(options_frame, "Notificaciones", notif_var, "🔔")
    create_checkbutton(options_frame, "Guardado Automático", auto_save_var, "💾")

    # Vista previa mejorada
    preview_frame = tk.Frame(right_panel, bg='#f8f9fa')
    preview_frame.pack(fill="both", expand=True, pady=(10, 0))

    tk.Label(preview_frame, text="Vista Previa:", 
             font=("Segoe UI", 10, "bold"),
             bg='#f8f9fa',
             fg=COLORS["dark"]).pack(anchor="w", pady=(0, 8))

    preview_canvas = tk.Canvas(preview_frame, width=160, height=120, 
                              bg="white", highlightthickness=2, 
                              highlightbackground=COLORS["gray"],
                              relief="flat")
    preview_canvas.pack(fill="both", expand=True)

    def update_preview():
        preview_canvas.delete("all")
        
        # Fondo basado en brillo
        brillo_val = brig_var.get()
        bg_color = f"#{int(255 * (brillo_val/100)):02x}{int(255 * (brillo_val/100)):02x}{int(255 * (brillo_val/100)):02x}"
        preview_canvas.config(bg=bg_color)
        
        # Elementos de preview basados en configuración
        if modo_noche.get():
            preview_canvas.create_text(80, 25, text="🌙 Modo Nocturno", font=("Segoe UI", 8, "bold"), fill="#4a90e2")
        else:
            preview_canvas.create_text(80, 25, text="☀️ Modo Diurno", font=("Segoe UI", 8, "bold"), fill="#2d3748")
        
        preview_canvas.create_rectangle(20, 40, 60, 60, outline="#48bb78" if auto_save_var.get() else "#cbd5e0", width=2)
        preview_canvas.create_text(45, 50, text="OK", font=("Segoe UI", 7), fill="#48bb78" if auto_save_var.get() else "#cbd5e0")
        
        preview_canvas.create_oval(100, 40, 140, 80, outline="#ed8936" if notif_var.get() else "#cbd5e0", width=2, fill="#fed7d7" if notif_var.get() else "#f7fafc")
        preview_canvas.create_text(120, 60, text="🔔", font=("Segoe UI", 8))

        # Barra de volumen
        vol_width = int(120 * (vol_var.get() / 100))
        preview_canvas.create_rectangle(20, 85, 140, 95, outline="#e2e8f0", fill="#e2e8f0")
        preview_canvas.create_rectangle(20, 85, 20 + vol_width, 95, outline="#4a90e2", fill="#4a90e2")

    # Botones de acción
    action_frame = tk.Frame(win, bg='#f8f9fa', pady=12, padx=16)
    action_frame.pack(fill="x", side="bottom")

    status_var = tk.StringVar(value="⚡ Listo para configurar")

    def create_action_button(parent, text, command, color, side="left"):
        btn = tk.Button(parent, text=text, command=command,
                       bg=color, fg="white", font=("Segoe UI", 10, "bold"),
                       relief="flat", bd=0, padx=20, pady=8,
                       cursor="hand2")
        
        # Efecto hover
        def on_enter(e):
            btn.config(bg=increase_brightness(color, 20))
        def on_leave(e):
            btn.config(bg=color)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        btn.pack(side=side, padx=5)
        return btn

    def increase_brightness(hex_color, factor):
        """Aumenta el brillo de un color hex"""
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        r = min(255, r + factor)
        g = min(255, g + factor)
        b = min(255, b + factor)
        return f"#{r:02x}{g:02x}{b:02x}"

    def restore_defaults():
        vol_var.set(50)
        brig_var.set(70)
        resolucion_var.set(50)
        modo_noche.set(False)
        notif_var.set(True)
        auto_save_var.set(True)
        status_var.set("🔄 Valores restaurados por defecto")
        update_preview()

    def save_settings():
        ajustes = {
            "volumen": vol_var.get(),
            "brillo": brig_var.get(),
            "resolucion": resolucion_var.get(),
            "modo_noche": modo_noche.get(),
            "notificaciones": notif_var.get(),
            "auto_guardado": auto_save_var.get()
        }
        print("💾 Ajustes guardados:", ajustes)
        status_var.set("✅ Ajustes guardados exitosamente")
        
        # 🔑 Llama al callback con el diccionario de ajustes
        if apply_settings_callback:
            apply_settings_callback(ajustes)

    # Botones de acción
    create_action_button(action_frame, "🔄 Restaurar", restore_defaults, COLORS["warning"], "left")
    create_action_button(action_frame, "💾 Guardar", save_settings, COLORS["success"], "right")

    # Barra de estado
    status_bar = tk.Label(action_frame, textvariable=status_var,
                         font=("Segoe UI", 9, "italic"),
                         bg='#f8f9fa', fg=COLORS["dark"])
    status_bar.pack(side="left", padx=(0, 20))

    # Atajos de teclado
    def _save_bind(e): 
        save_settings()
    win.bind('<Control-s>', _save_bind)
    win.bind('<Control-d>', lambda e: restore_defaults())
    win.bind('<Escape>', lambda e: win.destroy())

    # Tooltip de atajos
    win.bind('<F1>', lambda e: messagebox.showinfo("Atajos", 
        "Ctrl+S: Guardar ajustes\nCtrl+D: Restaurar valores\nEsc: Cerrar ventana"))

    # Inicializar vista previa
    update_preview()

    # Centrar ventana
    win.transient(parent)
    win.grab_set()
    
    return win