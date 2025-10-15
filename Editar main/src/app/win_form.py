import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from datetime import datetime

def open_win_form(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("📝 Formulario de Registro")
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

    def aumentar_brillo(hex_color, factor):
        """Aumenta el brillo de un color hex"""
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        r = min(255, r + factor)
        g = min(255, g + factor)
        b = min(255, b + factor)
        return f"#{r:02x}{g:02x}{b:02x}"

    # Frame principal
    main_frame = tk.Frame(win, bg=COLORS["light"], padx=25, pady=25)
    main_frame.pack(fill="both", expand=True)

    # Header
    header_frame = tk.Frame(main_frame, bg=COLORS["light"])
    header_frame.pack(fill="x", pady=(0, 20))

    tk.Label(header_frame, text="📝 FORMULARIO DE REGISTRO", 
             font=("Segoe UI", 16, "bold"),
             bg=COLORS["light"],
             fg=COLORS["primary"]).pack(side="left")

    tk.Label(header_frame, text="Completa tus datos personales",
             font=("Segoe UI", 10, "italic"),
             bg=COLORS["light"],
             fg=COLORS["dark"]).pack(side="left", padx=(10, 0))

    # Contenedor del formulario
    form_frame = tk.LabelFrame(main_frame, text=" INFORMACIÓN PERSONAL ", 
                              font=("Segoe UI", 11, "bold"),
                              bg=COLORS["light"],
                              fg=COLORS["dark"],
                              padx=20,
                              pady=20,
                              relief="groove",
                              bd=1)
    form_frame.pack(fill="both", expand=True, pady=(0, 20))

    # Configurar grid para el formulario
    form_frame.columnconfigure(1, weight=1)

    # Variables para los campos
    datos_formulario = {
        "nombre": tk.StringVar(),
        "edad": tk.StringVar(),
        "email": tk.StringVar(),
        "telefono": tk.StringVar(),
        "ciudad": tk.StringVar(),
        "ocupacion": tk.StringVar()
    }

    # Función de validación numérica
    def validar_numero(texto):
        """Valida que el texto sea un número válido"""
        if texto == "":
            return True
        try:
            int(texto)
            return True
        except ValueError:
            return False

    # Crear campos del formulario
    row = 0
    
    # Nombre
    tk.Label(form_frame, text="Nombre completo: *", 
             font=("Segoe UI", 10, "bold"),
             bg=COLORS["light"],
             fg=COLORS["primary"]).grid(row=row, column=0, sticky="w", pady=8, padx=(0, 10))
    
    ent_nombre = tk.Entry(form_frame, textvariable=datos_formulario["nombre"], 
                         font=("Segoe UI", 10),
                         bg="white", fg=COLORS["dark"],
                         relief="solid", bd=1,
                         width=30)
    ent_nombre.grid(row=row, column=1, sticky="ew", pady=8)
    row += 1

    # Edad
    tk.Label(form_frame, text="Edad: *", 
             font=("Segoe UI", 10, "bold"),
             bg=COLORS["light"],
             fg=COLORS["primary"]).grid(row=row, column=0, sticky="w", pady=8, padx=(0, 10))
    
    ent_edad = tk.Entry(form_frame, textvariable=datos_formulario["edad"],
                       font=("Segoe UI", 10),
                       bg="white", fg=COLORS["dark"],
                       relief="solid", bd=1,
                       width=10,
                       validate="key",
                       validatecommand=(win.register(validar_numero), '%P'))
    ent_edad.grid(row=row, column=1, sticky="w", pady=8)
    row += 1

    # Email
    tk.Label(form_frame, text="Correo electrónico:", 
             font=("Segoe UI", 10),
             bg=COLORS["light"],
             fg=COLORS["dark"]).grid(row=row, column=0, sticky="w", pady=8, padx=(0, 10))
    
    ent_email = tk.Entry(form_frame, textvariable=datos_formulario["email"],
                        font=("Segoe UI", 10),
                        bg="white", fg=COLORS["dark"],
                        relief="solid", bd=1,
                        width=30)
    ent_email.grid(row=row, column=1, sticky="ew", pady=8)
    row += 1

    # Teléfono
    tk.Label(form_frame, text="Teléfono:", 
             font=("Segoe UI", 10),
             bg=COLORS["light"],
             fg=COLORS["dark"]).grid(row=row, column=0, sticky="w", pady=8, padx=(0, 10))
    
    ent_telefono = tk.Entry(form_frame, textvariable=datos_formulario["telefono"],
                           font=("Segoe UI", 10),
                           bg="white", fg=COLORS["dark"],
                           relief="solid", bd=1,
                           width=15,
                           validate="key",
                           validatecommand=(win.register(validar_numero), '%P'))
    ent_telefono.grid(row=row, column=1, sticky="w", pady=8)
    row += 1

    # Ciudad
    tk.Label(form_frame, text="Ciudad:", 
             font=("Segoe UI", 10),
             bg=COLORS["light"],
             fg=COLORS["dark"]).grid(row=row, column=0, sticky="w", pady=8, padx=(0, 10))
    
    ent_ciudad = tk.Entry(form_frame, textvariable=datos_formulario["ciudad"],
                         font=("Segoe UI", 10),
                         bg="white", fg=COLORS["dark"],
                         relief="solid", bd=1,
                         width=20)
    ent_ciudad.grid(row=row, column=1, sticky="w", pady=8)
    row += 1

    # Ocupación
    tk.Label(form_frame, text="Ocupación:", 
             font=("Segoe UI", 10),
             bg=COLORS["light"],
             fg=COLORS["dark"]).grid(row=row, column=0, sticky="w", pady=8, padx=(0, 10))
    
    ent_ocupacion = tk.Entry(form_frame, textvariable=datos_formulario["ocupacion"],
                            font=("Segoe UI", 10),
                            bg="white", fg=COLORS["dark"],
                            relief="solid", bd=1,
                            width=25)
    ent_ocupacion.grid(row=row, column=1, sticky="w", pady=8)

    # Frame para botones
    button_frame = tk.Frame(main_frame, bg=COLORS["light"])
    button_frame.pack(fill="x", pady=(10, 0))

    def create_button(parent, text, command, color, icon="", width=12):
        btn = tk.Button(parent, text=f"{icon} {text}", command=command,
                       bg=color, fg="white", font=("Segoe UI", 10, "bold"),
                       relief="flat", bd=0, padx=15, pady=10,
                       cursor="hand2", width=width)
        
        # Efecto hover
        def on_enter(e):
            btn.config(bg=aumentar_brillo(color, 20))
        def on_leave(e):
            btn.config(bg=color)
        
        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)
        return btn

    def validar_formulario():
        """Valida todos los campos del formulario"""
        errores = []
        
        # Validar nombre
        nombre = datos_formulario["nombre"].get().strip()
        if not nombre:
            errores.append("📝 El nombre completo es obligatorio")
            ent_nombre.config(highlightbackground=COLORS["danger"], highlightcolor=COLORS["danger"])
        else:
            ent_nombre.config(highlightbackground=COLORS["success"], highlightcolor=COLORS["success"])
        
        # Validar edad
        edad_txt = datos_formulario["edad"].get().strip()
        if not edad_txt:
            errores.append("🎂 La edad es obligatoria")
            ent_edad.config(highlightbackground=COLORS["danger"], highlightcolor=COLORS["danger"])
        elif not edad_txt.isdigit():
            errores.append("🔢 La edad debe ser un número válido")
            ent_edad.config(highlightbackground=COLORS["danger"], highlightcolor=COLORS["danger"])
        elif int(edad_txt) < 1 or int(edad_txt) > 120:
            errores.append("📊 La edad debe estar entre 1 y 120 años")
            ent_edad.config(highlightbackground=COLORS["danger"], highlightcolor=COLORS["danger"])
        else:
            ent_edad.config(highlightbackground=COLORS["success"], highlightcolor=COLORS["success"])
        
        # Validar email si se proporciona
        email = datos_formulario["email"].get().strip()
        if email and "@" not in email:
            errores.append("📧 El formato del correo electrónico no es válido")
            ent_email.config(highlightbackground=COLORS["danger"], highlightcolor=COLORS["danger"])
        elif email:
            ent_email.config(highlightbackground=COLORS["success"], highlightcolor=COLORS["success"])
        
        return errores

    def limpiar_formulario():
        """Limpia todos los campos del formulario"""
        for variable in datos_formulario.values():
            variable.set("")
        
        # Resetear colores de borde
        for entry in [ent_nombre, ent_edad, ent_email, ent_telefono, ent_ciudad, ent_ocupacion]:
            entry.config(highlightbackground=COLORS["gray"], highlightcolor=COLORS["primary"])
        
        messagebox.showinfo("Formulario", "🧹 Todos los campos han sido limpiados")

    def mostrar_vista_previa():
        """Muestra una vista previa de los datos ingresados"""
        errores = validar_formulario()
        if errores:
            messagebox.showwarning("Vista Previa", 
                                 "⚠️ Complete los campos obligatorios para ver la vista previa")
            return
        
        vista_previa = f"📋 VISTA PREVIA DEL FORMULARIO\n\n"
        vista_previa += f"👤 Nombre: {datos_formulario['nombre'].get()}\n"
        vista_previa += f"🎂 Edad: {datos_formulario['edad'].get()} años\n"
        vista_previa += f"📧 Email: {datos_formulario['email'].get() or 'No proporcionado'}\n"
        vista_previa += f"📞 Teléfono: {datos_formulario['telefono'].get() or 'No proporcionado'}\n"
        vista_previa += f"🏙️ Ciudad: {datos_formulario['ciudad'].get() or 'No proporcionado'}\n"
        vista_previa += f"💼 Ocupación: {datos_formulario['ocupacion'].get() or 'No proporcionado'}\n"
        
        messagebox.showinfo("Vista Previa", vista_previa)

    def validar_y_guardar():
        """Valida y guarda los datos del formulario"""
        errores = validar_formulario()
        
        if errores:
            mensaje_error = "Se encontraron los siguientes errores:\n\n" + "\n• ".join(errores)
            messagebox.showerror("Error de Validación", mensaje_error)
            return
        
        # Si pasa la validación, proceder a guardar
        ruta = filedialog.asksaveasfilename(
            title="Guardar datos del formulario",
            defaultextension=".txt",
            filetypes=[
                ("Archivo de texto", "*.txt"),
                ("Archivo CSV", "*.csv"),
                ("Todos los archivos", "*.*")
            ],
            initialfile=f"formulario_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
        )
        
        if ruta:
            try:
                with open(ruta, "w", encoding="utf-8") as f:
                    f.write("=== FORMULARIO DE REGISTRO ===\n")
                    f.write(f"Fecha de registro: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n")
                    f.write("=" * 40 + "\n")
                    
                    campos = [
                        ("Nombre completo", datos_formulario["nombre"].get().strip()),
                        ("Edad", datos_formulario["edad"].get().strip()),
                        ("Correo electrónico", datos_formulario["email"].get().strip() or "No proporcionado"),
                        ("Teléfono", datos_formulario["telefono"].get().strip() or "No proporcionado"),
                        ("Ciudad", datos_formulario["ciudad"].get().strip() or "No proporcionado"),
                        ("Ocupación", datos_formulario["ocupacion"].get().strip() or "No proporcionado")
                    ]
                    
                    for campo, valor in campos:
                        f.write(f"{campo}: {valor}\n")
                    
                    f.write("=" * 40 + "\n")
                    f.write("✅ Registro completado exitosamente\n")
                
                messagebox.showinfo("✅ Éxito", 
                                  f"📁 Datos guardados correctamente en:\n{ruta}\n\n"
                                  f"📊 Resumen:\n"
                                  f"• Nombre: {datos_formulario['nombre'].get()}\n"
                                  f"• Edad: {datos_formulario['edad'].get()} años\n"
                                  f"• Registro: {datetime.now().strftime('%d/%m/%Y %H:%M')}")
                
            except Exception as e:
                messagebox.showerror("Error", f"No se pudo guardar el archivo:\n{str(e)}")

    # Crear botones
    btn_limpiar = create_button(button_frame, "Limpiar", limpiar_formulario, 
                               COLORS["warning"], "🧹")
    btn_limpiar.pack(side="left", padx=(0, 10))

    btn_vista_previa = create_button(button_frame, "Vista Previa", mostrar_vista_previa, 
                                    COLORS["purple"], "👁️")
    btn_vista_previa.pack(side="left", padx=(0, 10))

    btn_guardar = create_button(button_frame, "Guardar", validar_y_guardar, 
                               COLORS["success"], "💾")
    btn_guardar.pack(side="left", padx=(0, 10))

    btn_cerrar = create_button(button_frame, "Cerrar", win.destroy, 
                              COLORS["danger"], "🚪")
    btn_cerrar.pack(side="right")

    # Configurar bordes de validación
    for entry in [ent_nombre, ent_edad, ent_email, ent_telefono, ent_ciudad, ent_ocupacion]:
        entry.config(highlightthickness=2, highlightbackground=COLORS["gray"], highlightcolor=COLORS["primary"])

    # Atajos de teclado
    def on_enter_key(event):
        validar_y_guardar()

    win.bind("<Control-s>", on_enter_key)
    ent_nombre.bind("<Return>", lambda e: ent_edad.focus())
    ent_edad.bind("<Return>", lambda e: ent_email.focus())
    ent_email.bind("<Return>", lambda e: ent_telefono.focus())
    ent_telefono.bind("<Return>", lambda e: ent_ciudad.focus())
    ent_ciudad.bind("<Return>", lambda e: ent_ocupacion.focus())
    ent_ocupacion.bind("<Return>", on_enter_key)

    # Centrar ventana y hacerla modal
    win.transient(parent)
    win.grab_set()
    
    # Focus en el primer campo
    ent_nombre.focus()

    return win