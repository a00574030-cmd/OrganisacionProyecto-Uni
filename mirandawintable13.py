import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from tkcalendar import Calendar
import csv
from pathlib import Path
from datetime import datetime

CSV_PATH = Path(__file__).resolve().parents[1] / "data" / "calendario.csv"

# Colores modernos para la interfaz
COLORES = {
    "fondo_principal": "#2C3E50",
    "fondo_secundario": "#34495E",
    "fondo_calendario": "#ECF0F1",
    "texto_principal": "#FFFFFF",
    "texto_secundario": "#BDC3C7",
    "acento_verde": "#27AE60",
    "acento_rojo": "#E74C3C",
    "acento_amarillo": "#F39C12",
    "acento_azul": "#3498DB",
    "acento_morado": "#9B59B6",
    "borde": "#1ABC9C"
}

def cargar_eventos():
    """Carga eventos desde CSV y retorna diccionario con fechas como clave"""
    eventos = {}
    try:
        if CSV_PATH.exists():
            with open(CSV_PATH, "r", encoding="utf-8") as f:
                reader = csv.DictReader(f)
                for row in reader:
                    fecha = row["fecha"]
                    titulo = row["titulo"]
                    realizado = row.get("realizado", "False").lower() == "true"
                    
                    if fecha not in eventos:
                        eventos[fecha] = []
                    
                    eventos[fecha].append({
                        "titulo": titulo,
                        "realizado": realizado
                    })
        return eventos
    except Exception as e:
        messagebox.showerror("Error", f"Error al cargar eventos: {e}")
        return {}

def guardar_eventos(eventos):
    """Guarda todos los eventos en el archivo CSV"""
    try:
        CSV_PATH.parent.mkdir(parents=True, exist_ok=True)
        
        with open(CSV_PATH, "w", encoding="utf-8", newline='') as f:
            fieldnames = ["fecha", "titulo", "realizado"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            
            for fecha, tareas in eventos.items():
                for tarea in tareas:
                    writer.writerow({
                        "fecha": fecha,
                        "titulo": tarea["titulo"],
                        "realizado": str(tarea["realizado"])
                    })
        return True
    except Exception as e:
        messagebox.showerror("Error", f"Error al guardar eventos: {e}")
        return False

def crear_boton_estilizado(parent, text, command, color, width=15):
    """Crea un botón con estilo moderno"""
    btn = tk.Button(
        parent,
        text=text,
        command=command,
        bg=color,
        fg=COLORES["texto_principal"],
        font=("Arial", 10, "bold"),
        relief="flat",
        bd=0,
        padx=15,
        pady=8,
        width=width,
        cursor="hand2"
    )
    
    # Efecto hover
    def on_enter(e):
        btn.config(bg=self.aumentar_brillo(color, 20))
    
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

def open_win_table(parent: tk.Tk, year: int, month: int):
    """Abre ventana de calendario para mes y año específicos"""
    win = tk.Toplevel(parent)
    win.title(f"Calendario: {year}-{month:02}")
    win.geometry("700x650")
    win.configure(bg=COLORES["fondo_principal"])
    win.transient(parent)
    win.grab_set()

    # Configurar estilo ttk
    estilo = ttk.Style()
    estilo.theme_use('clam')
    
    # Configurar estilos personalizados
    estilo.configure(
        "Titulo.TLabel",
        background=COLORES["fondo_principal"],
        foreground=COLORES["texto_principal"],
        font=("Arial", 16, "bold")
    )
    
    estilo.configure(
        "Marco.TLabelframe",
        background=COLORES["fondo_principal"],
        foreground=COLORES["texto_principal"],
        font=("Arial", 11, "bold")
    )
    
    estilo.configure(
        "Marco.TLabelframe.Label",
        background=COLORES["fondo_principal"],
        foreground=COLORES["texto_principal"]
    )

    # Frame principal
    main_frame = tk.Frame(win, bg=COLORES["fondo_principal"])
    main_frame.pack(fill="both", expand=True, padx=15, pady=15)

    # Título
    titulo_frame = tk.Frame(main_frame, bg=COLORES["fondo_principal"])
    titulo_frame.pack(fill="x", pady=(0, 15))
    
    tk.Label(
        titulo_frame,
        text="📅 CALENDARIO DE TAREAS",
        font=("Arial", 18, "bold"),
        bg=COLORES["fondo_principal"],
        fg=COLORES["texto_principal"]
    ).pack(side="left")
    
    # Indicador de mes/año
    tk.Label(
        titulo_frame,
        text=f"{year} - {month:02d}",
        font=("Arial", 14, "italic"),
        bg=COLORES["fondo_principal"],
        fg=COLORES["acento_morado"]
    ).pack(side="right")

    eventos = cargar_eventos()
    fecha_seleccionada = None

    # Frame para calendario y tareas
    contenido_frame = tk.Frame(main_frame, bg=COLORES["fondo_principal"])
    contenido_frame.pack(fill="both", expand=True)

    # Calendario (lado izquierdo)
    calendario_frame = tk.Frame(contenido_frame, bg=COLORES["fondo_secundario"], relief="raised", bd=2)
    calendario_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

    # Título del calendario
    tk.Label(
        calendario_frame,
        text="CALENDARIO",
        font=("Arial", 12, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["acento_azul"],
        pady=10
    ).pack(fill="x")

    # Calendario personalizado
    cal = Calendar(
        calendario_frame,
        selectmode="day",
        year=year,
        month=month,
        day=1,
        date_pattern='yyyy-mm-dd',
        showweeknumbers=False,
        background=COLORES["fondo_calendario"],
        foreground=COLORES["fondo_principal"],
        selectbackground=COLORES["acento_morado"],
        selectforeground=COLORES["texto_principal"],
        normalbackground=COLORES["fondo_calendario"],
        normalforeground=COLORES["fondo_principal"],
        weekendbackground=COLORES["fondo_calendario"],
        weekendforeground=COLORES["acento_rojo"],
        headersbackground=COLORES["acento_azul"],
        headersforeground=COLORES["texto_principal"],
        bordercolor=COLORES["borde"],
        borderwidth=2,
        font=("Arial", 10),
        cursor="hand2"
    )
    cal.pack(padx=10, pady=10, fill="both", expand=True)

    def actualizar_resaltado_calendario():
        """Actualiza el resaltado de fechas con eventos en el calendario"""
        for event_id in cal.calevent_get():
            cal.calevent_delete(event_id)
        
        for fecha, tareas in eventos.items():
            try:
                total_tareas = len(tareas)
                tareas_realizadas = sum(1 for tarea in tareas if tarea["realizado"])
                
                if total_tareas > 0:
                    if tareas_realizadas == total_tareas:
                        cal.calevent_create(fecha, "✓ Todas realizadas", "todas_realizadas")
                    elif tareas_realizadas > 0:
                        cal.calevent_create(fecha, "⚡ Parcialmente", "parcial_realizado")
                    else:
                        cal.calevent_create(fecha, "📝 Pendientes", "pendientes")
            except Exception:
                pass
    
    # Configurar colores para los tags del calendario
    cal.tag_config("todas_realizadas", background=COLORES["acento_verde"], foreground=COLORES["texto_principal"])
    cal.tag_config("parcial_realizado", background=COLORES["acento_amarillo"], foreground=COLORES["fondo_principal"])
    cal.tag_config("pendientes", background=COLORES["acento_rojo"], foreground=COLORES["texto_principal"])

    # Tareas (lado derecho)
    tareas_frame = tk.Frame(contenido_frame, bg=COLORES["fondo_secundario"], relief="raised", bd=2)
    tareas_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

    # Título de tareas
    tk.Label(
        tareas_frame,
        text="📋 TAREAS DEL DÍA",
        font=("Arial", 12, "bold"),
        bg=COLORES["fondo_secundario"],
        fg=COLORES["acento_azul"],
        pady=10
    ).pack(fill="x")

    # Frame para la lista de tareas
    lista_tareas_frame = tk.Frame(tareas_frame, bg=COLORES["fondo_secundario"])
    lista_tareas_frame.pack(fill="both", expand=True, padx=10, pady=10)

    # Treeview para mostrar eventos con checkboxes
    style = ttk.Style()
    style.configure("Custom.Treeview",
        background=COLORES["fondo_calendario"],
        foreground=COLORES["fondo_principal"],
        fieldbackground=COLORES["fondo_calendario"],
        font=("Arial", 10)
    )
    style.configure("Custom.Treeview.Heading",
        background=COLORES["acento_azul"],
        foreground=COLORES["texto_principal"],
        font=("Arial", 10, "bold")
    )

    columns = ("realizado", "tarea")
    tree = ttk.Treeview(lista_tareas_frame, columns=columns, show="tree headings", 
                       height=12, style="Custom.Treeview")
    
    tree.heading("realizado", text="✓")
    tree.heading("tarea", text="TAREA")
    tree.column("realizado", width=60, anchor="center")
    tree.column("tarea", width=250, anchor="w")

    scrollbar = ttk.Scrollbar(lista_tareas_frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scrollbar.set)
    
    tree.pack(side="left", fill="both", expand=True)
    scrollbar.pack(side="right", fill="y")

    # Configurar tags para el treeview
    tree.tag_configure("realizada", foreground="#7F8C8D", font=("Arial", 9, "overstrike"))
    tree.tag_configure("pendiente", foreground=COLORES["fondo_principal"], font=("Arial", 9))

    def alternar_realizado(event):
        """Alterna el estado de realizado de una tarea al hacer clic"""
        item = tree.selection()
        if item:
            item = item[0]
            fecha = fecha_seleccionada
            if fecha and fecha in eventos:
                values = tree.item(item, "values")
                if values and values[1] != "No hay eventos para esta fecha":
                    tarea_texto = values[1]
                    
                    for i, tarea in enumerate(eventos[fecha]):
                        if tarea["titulo"] == tarea_texto:
                            eventos[fecha][i]["realizado"] = not eventos[fecha][i]["realizado"]
                            guardar_eventos(eventos)
                            actualizar_resaltado_calendario()
                            mostrar_eventos()
                            break

    tree.bind("<Double-1>", alternar_realizado)

    def agregar_tarea():
        """Agrega una nueva tarea para la fecha seleccionada"""
        if not fecha_seleccionada:
            messagebox.showwarning("Advertencia", "Por favor selecciona una fecha primero")
            return
        
        tarea = simpledialog.askstring("Nueva Tarea", "Ingresa la tarea:")
        if tarea and tarea.strip():
            if fecha_seleccionada not in eventos:
                eventos[fecha_seleccionada] = []
            
            eventos[fecha_seleccionada].append({
                "titulo": tarea.strip(),
                "realizado": False
            })
            
            if guardar_eventos(eventos):
                actualizar_resaltado_calendario()
                mostrar_eventos()
                messagebox.showinfo("Éxito", "✅ Tarea agregada correctamente")

    def eliminar_tarea():
        """Elimina la tarea seleccionada"""
        if not fecha_seleccionada:
            messagebox.showwarning("Advertencia", "Por favor selecciona una fecha primero")
            return
        
        item = tree.selection()
        if not item:
            messagebox.showwarning("Advertencia", "Por favor selecciona una tarea para eliminar")
            return
        
        item = item[0]
        values = tree.item(item, "values")
        if values and fecha_seleccionada in eventos and values[1] != "No hay eventos para esta fecha":
            tarea_texto = values[1]
            
            eventos[fecha_seleccionada] = [tarea for tarea in eventos[fecha_seleccionada] 
                                         if tarea["titulo"] != tarea_texto]
            
            if not eventos[fecha_seleccionada]:
                del eventos[fecha_seleccionada]
            
            if guardar_eventos(eventos):
                actualizar_resaltado_calendario()
                mostrar_eventos()
                messagebox.showinfo("Éxito", "🗑️ Tarea eliminada correctamente")

    def mostrar_eventos(event=None):
        """Muestra eventos para la fecha seleccionada"""
        nonlocal fecha_seleccionada
        fecha_sel = cal.get_date()
        fecha_seleccionada = fecha_sel
        
        for item in tree.get_children():
            tree.delete(item)
        
        lista_eventos = eventos.get(fecha_sel, [])
        
        if lista_eventos:
            for tarea in lista_eventos:
                estado = "✅" if tarea["realizado"] else "⭕"
                tags = ("realizada",) if tarea["realizado"] else ("pendiente",)
                tree.insert("", "end", values=(estado, tarea["titulo"]), tags=tags)
        else:
            tree.insert("", "end", values=("", "📭 No hay eventos para esta fecha"))

    # Frame de botones
    botones_frame = tk.Frame(main_frame, bg=COLORES["fondo_principal"])
    botones_frame.pack(fill="x", pady=15)

    crear_boton_estilizado(
        botones_frame, 
        "➕ AGREGAR TAREA", 
        agregar_tarea, 
        COLORES["acento_verde"],
        18
    ).pack(side="left", padx=5)

    crear_boton_estilizado(
        botones_frame, 
        "🗑️ ELIMINAR TAREA", 
        eliminar_tarea, 
        COLORES["acento_rojo"],
        18
    ).pack(side="left", padx=5)

    crear_boton_estilizado(
        botones_frame, 
        "📊 ESTADÍSTICAS", 
        lambda: mostrar_estadisticas(), 
        COLORES["acento_morado"],
        18
    ).pack(side="left", padx=5)

    crear_boton_estilizado(
        botones_frame, 
        "🚪 CERRAR", 
        win.destroy, 
        COLORES["acento_azul"],
        18
    ).pack(side="right", padx=5)

    def mostrar_estadisticas():
        """Muestra estadísticas de las tareas"""
        total_tareas = 0
        tareas_realizadas = 0
        
        for tareas in eventos.values():
            total_tareas += len(tareas)
            tareas_realizadas += sum(1 for tarea in tareas if tarea["realizado"])
        
        porcentaje = (tareas_realizadas / total_tareas * 100) if total_tareas > 0 else 0
        
        messagebox.showinfo(
            "📊 Estadísticas", 
            f"Total de tareas: {total_tareas}\n"
            f"Tareas realizadas: {tareas_realizadas}\n"
            f"Tareas pendientes: {total_tareas - tareas_realizadas}\n"
            f"Progreso: {porcentaje:.1f}%"
        )

    # Vincular eventos
    cal.bind("<<CalendarSelected>>", mostrar_eventos)

    # Inicializar
    actualizar_resaltado_calendario()
    win.after(100, mostrar_eventos)

    return win

# Función de prueba mejorada
if __name__ == "__main__":
    def main():
        root = tk.Tk()
        root.title("Calendario de Tareas - Inicio")
        root.geometry("400x300")
        root.configure(bg=COLORES["fondo_principal"])
        
        # Frame principal de inicio
        inicio_frame = tk.Frame(root, bg=COLORES["fondo_principal"])
        inicio_frame.pack(expand=True, fill="both", padx=20, pady=20)
        
        tk.Label(
            inicio_frame,
            text="🎯 CALENDARIO DE TAREAS",
            font=("Arial", 20, "bold"),
            bg=COLORES["fondo_principal"],
            fg=COLORES["texto_principal"],
            pady=20
        ).pack()
        
        tk.Label(
            inicio_frame,
            text="Organiza tus tareas de manera eficiente",
            font=("Arial", 12),
            bg=COLORES["fondo_principal"],
            fg=COLORES["texto_secundario"],
            pady=10
        ).pack()
        
        def abrir_calendario_actual():
            hoy = datetime.now()
            open_win_table(root, hoy.year, hoy.month)
        
        # Botones de inicio con estilo
        btn_frame = tk.Frame(inicio_frame, bg=COLORES["fondo_principal"])
        btn_frame.pack(pady=30)
        
        crear_boton_estilizado(
            btn_frame, 
            "📅 CALENDARIO ACTUAL", 
            abrir_calendario_actual, 
            COLORES["acento_verde"],
            20
        ).pack(pady=10)
        
        crear_boton_estilizado(
            btn_frame, 
            "🔮 OCTUBRE 2025", 
            lambda: open_win_table(root, 2025, 10), 
            COLORES["acento_morado"],
            20
        ).pack(pady=10)
        
        crear_boton_estilizado(
            btn_frame, 
            "❌ SALIR", 
            root.quit, 
            COLORES["acento_rojo"],
            20
        ).pack(pady=10)
        
        root.mainloop()

    main()
