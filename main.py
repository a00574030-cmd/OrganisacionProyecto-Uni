import tkinter as tk
from tkinter import ttk
from app.win_home import open_win_home
from app.win_form import open_win_form
from app.win_list import open_win_list
from app.win_table import open_win_table
from app.win_canvas import open_win_canvas 

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Proyecto Integrador - MVP")
        self.geometry("420x420")
        self.minsize(350, 300)

        self.current_volume = tk.DoubleVar(value=50.0)
        self.current_res = tk.StringVar(value="Resolución: 420x420")
        self.current_theme_var = tk.StringVar(value="Tema: Claro")
        
        # 🔑 Sistema de Estilos TTK
        self.style = ttk.Style(self)
        self.style.theme_use('clam') 
        
        # Define los colores clave para los dos temas
        self.COLORS = {
            "light": {"bg": '#f0f0f0', "fg": '#000000', "btn_bg": '#e0e0e0'},
            "dark": {"bg": '#1e1e1e', "fg": '#ffffff', "btn_bg": '#404040'}
        }
        
        self.apply_theme("light") # Aplicar tema inicial

        self.create_widgets()

    def apply_theme(self, theme_name):
        """Aplica un tema global (Claro o Oscuro) reconfigurando TTK."""
        
        colors = self.COLORS[theme_name]
        
        # 1. Aplicar a la ventana raíz (solo acepta 'bg', no estilo TTK)
        self.config(bg=colors["bg"])
        
        # 2. Reconfigurar estilos TTK básicos (esto afecta a todas las ventanas abiertas y futuras)
        self.style.configure('.', background=colors["bg"], foreground=colors["fg"]) # Estilo base
        self.style.configure('TFrame', background=colors["bg"])
        self.style.configure('TLabel', background=colors["bg"], foreground=colors["fg"])
        self.style.configure('TButton', background=colors["btn_bg"], foreground=colors["fg"])
        
        # 3. Forzar la actualización de todos los widgets (a veces necesario)
        self.event_generate("<<ThemeChanged>>")
        
        self.current_theme_var.set(f"Tema: {theme_name.capitalize()}")
        
        # Si ya existe el main_frame, asegurar que su fondo se actualice
        if hasattr(self, 'main_frame'):
            self.main_frame.config(style='TFrame') 
            
    def create_widgets(self):
        # 🔑 Usamos solo el estilo base 'TFrame' para que los cambios de apply_theme lo afecten.
        self.main_frame = ttk.Frame(self, padding=16) 
        self.main_frame.pack(fill="both", expand=True)
        
        # --- Widgets de Estado ---
        ttk.Label(self.main_frame, text="Estado Actual", font=("Segoe UI", 10, "italic")).pack(pady=(0, 5))
        
        self.vol_label = ttk.Label(self.main_frame, textvariable=self.current_volume)
        self.vol_label.pack()
        self.current_volume.set(f"Volumen: 50")
        
        self.res_label = ttk.Label(self.main_frame, textvariable=self.current_res)
        self.res_label.pack()
        
        self.theme_label = ttk.Label(self.main_frame, textvariable=self.current_theme_var)
        self.theme_label.pack(pady=(0, 10))

        # Canvas para simular el brillo (no es TTK, por eso necesita manejo separado)
        self.brillo_canvas = tk.Canvas(self.main_frame, width=30, height=10, highlightthickness=0, bg="#BBBBBB")
        self.brillo_canvas.pack(pady=(5, 12))
        
        ttk.Separator(self.main_frame).pack(pady=6, fill="x")
        
        # --- Botones de Navegación (Usando Ventanas Originales) ---
        ttk.Label(self.main_frame, text="Aplicación Demo (ttk)", font=("Segoe UI", 12, "bold")).pack(pady=(0, 12))
        
        # 🔑 Usamos los comandos originales sin pasar argumentos adicionales
        ttk.Button(self.main_frame, text="1) Home / Bienvenida", command=lambda: open_win_home(self)).pack(pady=4, fill="x")
        ttk.Button(self.main_frame, text="2) Formulario", command=lambda: open_win_form(self)).pack(pady=4, fill="x")
        ttk.Button(self.main_frame, text="3) Lista (CRUD básico)", command=lambda: open_win_list(self)).pack(pady=4, fill="x")
        ttk.Button(self.main_frame, text="4) Tabla (Treeview)", command=lambda: open_win_table(self)).pack(pady=4, fill="x")
        
        # Botón de ajustes - Pasamos el callback
        ttk.Button(self.main_frame, text="5) Ajustes / Canvas", 
                   command=lambda: open_win_canvas(self, apply_settings_callback=self.apply_settings)).pack(pady=4, fill="x")
        
        ttk.Separator(self.main_frame).pack(pady=6, fill="x")
        ttk.Button(self.main_frame, text="Salir", command=self.destroy).pack(pady=6)


    # 🔑 FUNCIÓN DE ENLACE GLOBAL
    def apply_settings(self, settings: dict):
        print(f"✅ Aplicando ajustes globales: {settings}")
        
        # --- 1. MODO NOCTURNO (Cambia el tema TTK global) ---
        if settings.get("modo_noche"):
            self.apply_theme("dark")
        else:
            self.apply_theme("light")
        
        # --- 2. BRILLO (Solo simulación en el Canvas) ---
        new_brillo = settings.get("brillo", 70)
        color_val = int(255 * (new_brillo / 100))
        brillo_color = f"#{color_val:02x}{color_val:02x}{color_val:02x}"
        self.brillo_canvas.config(bg=brillo_color)

        # --- 3. RESOLUCIÓN (Cambia el tamaño de la ventana) ---
        new_res = settings.get("resolucion", 50)
        width = int(350 + 4.5 * new_res) 
        height = int(300 + 3 * new_res) 
        self.geometry(f"{width}x{height}")
        self.current_res.set(f"Resolución: {width}x{height}")
        
        # --- 4. Volumen (Simulado) ---
        new_vol = settings.get("volumen", 50)
        self.current_volume.set(f"Volumen: {new_vol:.0f}") 


def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()