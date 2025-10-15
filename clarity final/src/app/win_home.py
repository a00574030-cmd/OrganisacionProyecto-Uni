import tkinter as tk
from tkinter import ttk, messagebox
from datetime import datetime

def open_win_home(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("🏠 Home / Bienvenida")
    win.geometry("500x450")
    win.configure(bg='#f8f9fa')
    win.minsize(450, 400)

    # Colores coherentes con la aplicación principal
    COLORS = {
        "primary": "#4a90e2",
        "success": "#48bb78", 
        "warning": "#ed8936",
        "danger": "#f56565",
        "light": "#f8f9fa",
        "dark": "#2d3748",
        "gray": "#e2e8f0",
        "purple": "#9f7aea"
    }

    # Frame principal
    main_frame = tk.Frame(win, bg=COLORS["light"], padx=25, pady=25)
    main_frame.pack(fill="both", expand=True)

    # Header
    header_frame = tk.Frame(main_frame, bg=COLORS["light"])
    header_frame.pack(fill="x", pady=(0, 20))

    tk.Label(header_frame, text="🏠 INICIO / BIENVENIDA", 
             font=("Segoe UI", 16, "bold"),
             bg=COLORS["light"],
             fg=COLORS["primary"]).pack(side="left")

    # Fecha y hora actual
    time_frame = tk.Frame(header_frame, bg=COLORS["light"])
    time_frame.pack(side="right")
    
    current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
    time_label = tk.Label(time_frame, text=f"🕒 {current_time}", 
                         font=("Segoe UI", 9),
                         bg=COLORS["light"],
                         fg=COLORS["dark"])
    time_label.pack()

    # Mensaje de bienvenida
    welcome_frame = tk.Frame(main_frame, bg=COLORS["light"])
    welcome_frame.pack(fill="x", pady=(0, 25))

    tk.Label(welcome_frame, text="¡Bienvenid@ al Sistema de Gestión!", 
             font=("Segoe UI", 14, "bold"),
             bg=COLORS["light"],
             fg=COLORS["dark"]).pack(pady=(0, 8))

    tk.Label(welcome_frame, text="Organiza tus tareas, metas y actividades de manera eficiente",
             font=("Segoe UI", 10),
             bg=COLORS["light"],
             fg=COLORS["dark"],
             wraplength=400).pack()

    # Panel de herramientas rápidas
    tools_frame = tk.LabelFrame(main_frame, text="🛠️ HERRAMIENTAS RÁPIDAS", 
                               font=("Segoe UI", 11, "bold"),
                               bg=COLORS["light"],
                               fg=COLORS["dark"],
                               padx=20,
                               pady=20)
    tools_frame.pack(fill="both", expand=True, pady=(0, 20))

    def create_tool_button(parent, text, description, command, color, icon=""):
        btn_frame = tk.Frame(parent, bg=COLORS["light"])
        btn_frame.pack(fill="x", pady=8)
        
        btn = tk.Button(btn_frame, text=f"{icon} {text}", command=command,
                       bg=color, fg="white", font=("Segoe UI", 10, "bold"),
                       relief="flat", bd=0, padx=20, pady=12,
                       cursor="hand2", width=15)
        btn.pack(side="left")
        
        desc_label = tk.Label(btn_frame, text=description,
                             font=("Segoe UI", 9),
                             bg=COLORS["light"],
                             fg=COLORS["dark"],
                             wraplength=250,
                             justify="left")
        desc_label.pack(side="left", padx=(15, 0), fill="x", expand=True)
        
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

    # Crear botones de herramientas
    create_tool_button(tools_frame, "🎯 Metas", 
                      "Gestiona tus objetivos y tareas pendientes", 
                      lambda: messagebox.showinfo("🎯 Metas", 
                                                "¡Acceso directo a tu lista de metas!\n\n"
                                                "Aquí podrás:\n• Agregar nuevas metas\n• Marcar como completadas\n• Organizar por prioridad"),
                      COLORS["success"])

    create_tool_button(tools_frame, "📅 Calendario", 
                      "Visualiza y organiza tus eventos y fechas importantes", 
                      lambda: messagebox.showinfo("📅 Calendario", 
                                                "¡Tu calendario personal!\n\n"
                                                "Funcionalidades:\n• Ver eventos del mes\n• Agregar nuevas citas\n• Recordatorios automáticos"),
                      COLORS["primary"])

    create_tool_button(tools_frame, "📢 Anuncios", 
                      "Mantente informado con las últimas actualizaciones", 
                      lambda: messagebox.showinfo("📢 Anuncios", 
                                                "¡Centro de información!\n\n"
                                                "Próximamente:\n• Noticias importantes\n• Actualizaciones del sistema\n• Recordatorios del equipo"),
                      COLORS["warning"])

    # Panel de estadísticas rápidas
    stats_frame = tk.LabelFrame(main_frame, text="📊 VISTA RÁPIDA", 
                               font=("Segoe UI", 11, "bold"),
                               bg=COLORS["light"],
                               fg=COLORS["dark"],
                               padx=20,
                               pady=15)
    stats_frame.pack(fill="x", pady=(0, 20))

    stats_grid = tk.Frame(stats_frame, bg=COLORS["light"])
    stats_grid.pack(fill="x")

    def create_stat_item(parent, text, value, color, icon, row, col):
        stat_frame = tk.Frame(parent, bg=COLORS["light"])
        stat_frame.grid(row=row, column=col, sticky="w", padx=(0, 30), pady=5)
        
        tk.Label(stat_frame, text=f"{icon} {text}", 
                font=("Segoe UI", 9, "bold"),
                bg=COLORS["light"],
                fg=COLORS["dark"]).pack(anchor="w")
        
        tk.Label(stat_frame, text=value, 
                font=("Segoe UI", 12, "bold"),
                bg=COLORS["light"],
                fg=color).pack(anchor="w")

    create_stat_item(stats_grid, "Metas Activas", "5", COLORS["success"], "✅", 0, 0)
    create_stat_item(stats_grid, "Pendientes", "3", COLORS["warning"], "⏳", 0, 1)
    create_stat_item(stats_grid, "Completadas", "12", COLORS["primary"], "🎯", 0, 2)
    create_stat_item(stats_grid, "Eventos Hoy", "2", COLORS["purple"], "📅", 1, 0)

    # Footer con botones de acción
    footer_frame = tk.Frame(main_frame, bg=COLORS["light"])
    footer_frame.pack(fill="x")

    def create_action_button(parent, text, command, color, icon=""):
        btn = tk.Button(parent, text=f"{icon} {text}", command=command,
                       bg=color, fg="white", font=("Segoe UI", 9, "bold"),
                       relief="flat", bd=0, padx=15, pady=8,
                       cursor="hand2")
        
        def on_enter(e):
            btn.config(bg=aumentar_brillo(color, 20))
        def on_leave(e):
            btn.config(bg=color)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    # Botones de acción
    btn_help = create_action_button(footer_frame, "Ayuda", 
                                   lambda: messagebox.showinfo("💡 Ayuda", 
                                                             "¿Necesitas ayuda?\n\n"
                                                             "• Metas: Organiza tus objetivos\n"
                                                             "• Calendario: Gestiona tu tiempo\n"
                                                             "• Formularios: Registra información\n"
                                                             "• Ajustes: Personaliza la app"),
                                   COLORS["primary"], "💡")
    btn_help.pack(side="left", padx=(0, 10))

    btn_about = create_action_button(footer_frame, "Acerca de", 
                                    lambda: messagebox.showinfo("ℹ️ Acerca de", 
                                                              "Sistema de Gestión Integral\n\n"
                                                              "Versión: 2.0.0\n"
                                                              "Desarrollado con Python & Tkinter\n"
                                                              "© 2024 - Todos los derechos reservados"),
                                    COLORS["purple"], "ℹ️")
    btn_about.pack(side="left", padx=(0, 10))

    btn_close = create_action_button(footer_frame, "Cerrar", win.destroy,
                                    COLORS["danger"], "🚪")
    btn_close.pack(side="right")

    # Actualizar la hora cada minuto
    def update_time():
        current_time = datetime.now().strftime("%d/%m/%Y %H:%M")
        time_label.config(text=f"🕒 {current_time}")
        win.after(60000, update_time)  # Actualizar cada minuto

    update_time()

    # Centrar ventana y hacerla modal
    win.transient(parent)
    win.grab_set()

    return win