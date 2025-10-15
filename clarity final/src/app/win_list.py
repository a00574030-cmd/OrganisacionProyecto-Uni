import tkinter as tk
from tkinter import ttk, messagebox

def open_win_list(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("🎯 Lista de Metas")
    win.geometry("650x550")
    win.configure(bg='#f8f9fa')
    win.minsize(600, 500)

    # Colores coherentes con la aplicación principal
    COLORS = {
        "primary": "#4a90e2",
        "success": "#48bb78", 
        "warning": "#ed8936",
        "danger": "#f56565",
        "light": "#f8f9fa",
        "dark": "#2d3748",
        "gray": "#e2e8f0"
    }

    # Frame principal
    main_frame = tk.Frame(win, bg=COLORS["light"], padx=20, pady=20)
    main_frame.pack(fill="both", expand=True)

    # Header
    header_frame = tk.Frame(main_frame, bg=COLORS["light"])
    header_frame.pack(fill="x", pady=(0, 20))

    tk.Label(header_frame, text="🎯 LISTA DE METAS", 
             font=("Segoe UI", 16, "bold"),
             bg=COLORS["light"],
             fg=COLORS["primary"]).pack(side="left")

    tk.Label(header_frame, text="Organiza y gestiona tus objetivos",
             font=("Segoe UI", 10, "italic"),
             bg=COLORS["light"],
             fg=COLORS["dark"]).pack(side="left", padx=(10, 0))

    # Contenido principal en dos columnas
    content_frame = tk.Frame(main_frame, bg=COLORS["light"])
    content_frame.pack(fill="both", expand=True)

    # Panel izquierdo - Entrada y controles
    left_panel = tk.Frame(content_frame, bg=COLORS["light"], width=200)
    left_panel.pack(side="left", fill="y", padx=(0, 15))
    left_panel.pack_propagate(False)

    # Panel derecho - Listas
    right_panel = tk.Frame(content_frame, bg=COLORS["light"])
    right_panel.pack(side="right", fill="both", expand=True)

    # Entrada de nueva meta
    input_frame = tk.LabelFrame(left_panel, text="➕ NUEVA META", 
                               font=("Segoe UI", 10, "bold"),
                               bg=COLORS["light"],
                               fg=COLORS["dark"],
                               padx=10,
                               pady=10)
    input_frame.pack(fill="x", pady=(0, 15))

    ent_item = tk.Entry(input_frame, font=("Segoe UI", 10), 
                       bg="white", fg=COLORS["dark"],
                       relief="solid", bd=1)
    ent_item.pack(fill="x", pady=(0, 10))
    ent_item.focus()

    def create_button(parent, text, command, color, icon="", width=15):
        btn = tk.Button(parent, text=f"{icon} {text}", command=command,
                       bg=color, fg="white", font=("Segoe UI", 10, "bold"),
                       relief="flat", bd=0, padx=15, pady=8,
                       cursor="hand2", width=width)
        
        # Efecto hover
        def on_enter(e):
            btn.config(bg=aumentar_brillo(color, 20))
        def on_leave(e):
            btn.config(bg=color)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    def aumentar_brillo(hex_color, factor):
        """Aumenta el brillo de un color hex"""
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        r = min(255, r + factor)
        g = min(255, g + factor)
        b = min(255, b + factor)
        return f"#{r:02x}{g:02x}{b:02x}"

    # Botones de acción
    btn_agregar = create_button(input_frame, "Agregar Meta", lambda: agregar(), 
                               COLORS["success"], "✅")
    btn_agregar.pack(fill="x", pady=2)

    # Frame para botones de control
    control_frame = tk.LabelFrame(left_panel, text="⚙️ CONTROLES", 
                                 font=("Segoe UI", 10, "bold"),
                                 bg=COLORS["light"],
                                 fg=COLORS["dark"],
                                 padx=10,
                                 pady=10)
    control_frame.pack(fill="x", pady=(0, 15))

    btn_eliminar = create_button(control_frame, "Eliminar", lambda: eliminar(), 
                                COLORS["danger"], "🗑️")
    btn_eliminar.pack(fill="x", pady=4)

    btn_terminar = create_button(control_frame, "Marcar como Terminada", 
                                lambda: terminar_tarea(), COLORS["primary"], "✅")
    btn_terminar.pack(fill="x", pady=4)

    btn_limpiar = create_button(control_frame, "Limpiar Pendientes", 
                               lambda: limpiar(), COLORS["warning"], "🧹")
    btn_limpiar.pack(fill="x", pady=4)

    # Estadísticas
    stats_frame = tk.LabelFrame(left_panel, text="📊 ESTADÍSTICAS", 
                               font=("Segoe UI", 10, "bold"),
                               bg=COLORS["light"],
                               fg=COLORS["dark"],
                               padx=10,
                               pady=10)
    stats_frame.pack(fill="x", pady=(0, 15))

    stats_text = tk.StringVar()
    stats_text.set("Pendientes: 0\nTerminadas: 0\nTotal: 0")

    stats_label = tk.Label(stats_frame, textvariable=stats_text,
                          font=("Segoe UI", 9),
                          bg=COLORS["light"],
                          fg=COLORS["dark"],
                          justify="left")
    stats_label.pack(anchor="w")

    # Lista de metas pendientes
    pending_frame = tk.LabelFrame(right_panel, text="📝 METAS PENDIENTES", 
                                 font=("Segoe UI", 11, "bold"),
                                 bg=COLORS["light"],
                                 fg=COLORS["dark"],
                                 padx=10,
                                 pady=10)
    pending_frame.pack(fill="both", expand=True, pady=(0, 15))

    # Frame para lista con scroll
    list_frame = tk.Frame(pending_frame, bg=COLORS["light"])
    list_frame.pack(fill="both", expand=True)

    lb = tk.Listbox(list_frame, 
                   font=("Segoe UI", 10),
                   bg="white",
                   fg=COLORS["dark"],
                   selectbackground=COLORS["primary"],
                   selectforeground="white",
                   relief="solid",
                   bd=1,
                   height=12)
    
    scrollbar = tk.Scrollbar(list_frame, orient="vertical", command=lb.yview)
    lb.configure(yscrollcommand=scrollbar.set)
    
    lb.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Lista de metas terminadas
    done_frame = tk.LabelFrame(right_panel, text="✅ METAS TERMINADAS", 
                              font=("Segoe UI", 11, "bold"),
                              bg=COLORS["light"],
                              fg=COLORS["dark"],
                              padx=10,
                              pady=10)
    done_frame.pack(fill="x")

    # Frame para lista terminada con scroll
    done_list_frame = tk.Frame(done_frame, bg=COLORS["light"])
    done_list_frame.pack(fill="x")

    lb_done = tk.Listbox(done_list_frame,
                        font=("Segoe UI", 10),
                        bg="#f0fff4",
                        fg="#2d3748",
                        selectbackground=COLORS["success"],
                        selectforeground="white",
                        relief="solid",
                        bd=1,
                        height=6)
    
    scrollbar_done = tk.Scrollbar(done_list_frame, orient="vertical", command=lb_done.yview)
    lb_done.configure(yscrollcommand=scrollbar_done.set)
    
    lb_done.pack(side="left", fill="both", expand=True)
    scrollbar_done.pack(side="right", fill="y")

    # Botón para limpiar terminadas
    btn_limpiar_terminadas = create_button(done_frame, "Limpiar Terminadas", 
                                         lambda: limpiar_terminadas(), 
                                         COLORS["warning"], "🧹")
    btn_limpiar_terminadas.pack(fill="x", pady=(10, 0))

    # Footer con botón cerrar
    footer_frame = tk.Frame(main_frame, bg=COLORS["light"])
    footer_frame.pack(fill="x", pady=(20, 0))

    btn_cerrar = create_button(footer_frame, "Cerrar", win.destroy, 
                              COLORS["danger"], "🚪", 10)
    btn_cerrar.pack(side="right")

    # Funciones de la aplicación
    def actualizar_estadisticas():
        pendientes = lb.size()
        terminadas = lb_done.size()
        total = pendientes + terminadas
        
        stats_text.set(f"📋 Pendientes: {pendientes}\n✅ Terminadas: {terminadas}\n📊 Total: {total}")

    def agregar():
        v = ent_item.get().strip()
        if v:
            lb.insert("end", f"• {v}")
            ent_item.delete(0, "end")
            actualizar_estadisticas()
            messagebox.showinfo("Éxito", "✅ Meta agregada correctamente")
        else:
            messagebox.showwarning("Aviso", "📝 Escribe un texto para agregar.")

    def eliminar():
        sel = lb.curselection()
        if sel:
            meta = lb.get(sel[0])
            lb.delete(sel[0])
            actualizar_estadisticas()
            messagebox.showinfo("Eliminado", f"🗑️ Meta eliminada: {meta}")
        else:
            messagebox.showwarning("Aviso", "👉 Selecciona una meta para eliminar.")

    def terminar_tarea():
        sel = lb.curselection()
        if sel:
            tarea = lb.get(sel[0])
            lb.delete(sel[0])
            lb_done.insert("end", f"✓ {tarea[2:]}")  # Remover el "• " inicial
            actualizar_estadisticas()
            messagebox.showinfo("¡Felicidades!", f"🎉 Meta completada: {tarea[2:]}")
        else:
            messagebox.showwarning("Aviso", "👉 Selecciona una meta para marcar como terminada.")

    def limpiar():
        if lb.size() > 0:
            respuesta = messagebox.askyesno("Confirmar", 
                                          "¿Estás seguro de que quieres limpiar todas las metas pendientes?")
            if respuesta:
                lb.delete(0, "end")
                actualizar_estadisticas()
                messagebox.showinfo("Listo", "🧹 Todas las metas pendientes han sido eliminadas")
        else:
            messagebox.showinfo("Info", "No hay metas pendientes para limpiar")

    def limpiar_terminadas():
        if lb_done.size() > 0:
            respuesta = messagebox.askyesno("Confirmar", 
                                          "¿Estás seguro de que quieres limpiar todas las metas terminadas?")
            if respuesta:
                lb_done.delete(0, "end")
                actualizar_estadisticas()
                messagebox.showinfo("Listo", "🧹 Todas las metas terminadas han sido eliminadas")
        else:
            messagebox.showinfo("Info", "No hay metas terminadas para limpiar")

    # Atajos de teclado
    def on_enter_key(event):
        agregar()

    ent_item.bind("<Return>", on_enter_key)

    def on_delete_key(event):
        eliminar()

    lb.bind("<Delete>", on_delete_key)

    def on_double_click(event):
        terminar_tarea()

    lb.bind("<Double-Button-1>", on_double_click)

    # Inicializar estadísticas
    actualizar_estadisticas()

    # Centrar ventana y hacerla modal
    win.transient(parent)
    win.grab_set()

    return win