import tkinter as tk
from tkinter import ttk
from app.win_home import open_win_home
from app.win_form import open_win_form
from app.win_list import open_win_list
from app.win_table import open_win_table
from app.win_canvas import open_win_canvas 
from datetime import datetime

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("🎯 Proyecto Integrador - MVP")
        self.geometry("450x500")
        self.minsize(400, 450)

        self.current_volume = tk.DoubleVar(value=50.0)
        self.current_theme_var = tk.StringVar(value="🎨 Tema: Claro")
        
        # 🔑 Sistema de Estilos TTK Mejorado
        self.style = ttk.Style(self)
        self.style.theme_use('clam') 
        
        # Define los colores clave para los dos temas
        self.COLORS = {
            "light": {
                "bg": '#f8f9fa', 
                "fg": '#2d3748', 
                "btn_bg": '#4a90e2',
                "btn_fg": '#ffffff',
                "accent": '#3182ce',
                "secondary": '#e2e8f0',
                "header_bg": '#4a90e2',
                "header_fg": '#ffffff'
            },
            "dark": {
                "bg": '#1a202c', 
                "fg": '#e2e8f0', 
                "btn_bg": '#2d3748',
                "btn_fg": '#ffffff',
                "accent": '#4299e1',
                "secondary": '#2d3748',
                "header_bg": '#2d3748',
                "header_fg": '#ffffff'
            }
        }
        
        self.apply_theme("light") # Aplicar tema inicial
        self.create_widgets()

    def apply_theme(self, theme_name):
        """Aplica un tema global (Claro u Oscuro) reconfigurando TTK."""
        
        colors = self.COLORS[theme_name]
        
        # Configurar ventana principal
        self.config(bg=colors["bg"])
        
        # Configurar estilos TTK
        self.style.configure('.', 
                           background=colors["bg"], 
                           foreground=colors["fg"],
                           font=('Segoe UI', 10))
        
        self.style.configure('TFrame', background=colors["bg"])
        self.style.configure('TLabel', background=colors["bg"], foreground=colors["fg"])
        self.style.configure('TLabelframe', background=colors["bg"], foreground=colors["fg"])
        self.style.configure('TLabelframe.Label', background=colors["bg"], foreground=colors["fg"])
        
        # Botones con estilo moderno
        self.style.configure('TButton',
                           background=colors["btn_bg"],
                           foreground=colors["btn_fg"],
                           borderwidth=0,
                           focuscolor='none',
                           font=('Segoe UI', 10, 'bold'))
        
        self.style.map('TButton',
                      background=[('active', colors["accent"]),
                                ('pressed', colors["accent"])])
        
        # Separadores
        self.style.configure('TSeparator', background=colors["secondary"])
        
        self.event_generate("<<ThemeChanged>>")
        self.current_theme_var.set(f"🎨 Tema: {theme_name.capitalize()}")
            
    def create_widgets(self):
        # Frame principal con mejor padding
        self.main_frame = ttk.Frame(self, padding=20) 
        self.main_frame.pack(fill="both", expand=True)
        
        # Header mejorado
        header_frame = ttk.Frame(self.main_frame)
        header_frame.pack(fill="x", pady=(0, 15))
        
        title_label = ttk.Label(header_frame, 
                               text="🚀 Proyecto Integrador", 
                               font=("Segoe UI", 16, "bold"),
                               foreground=self.COLORS["light"]["accent"])
        title_label.pack(side="top", pady=(0, 5))
        
        subtitle_label = ttk.Label(header_frame, 
                                  text="Sistema de Gestión MVP", 
                                  font=("Segoe UI", 10, "italic"))
        subtitle_label.pack(side="top")
        
        # Panel de estado actual mejorado
        status_frame = ttk.LabelFrame(self.main_frame, text="📊 Estado Actual", padding=12)
        status_frame.pack(fill="x", pady=(0, 15))
        
        # Información de estado en grid
        status_grid = ttk.Frame(status_frame)
        status_grid.pack(fill="x")
        
        # Fecha actual
        current_date = datetime.now().strftime("%d/%m/%Y")
        date_label = ttk.Label(status_grid, text=f"📅 {current_date}", 
                              font=("Segoe UI", 9))
        date_label.grid(row=0, column=0, sticky="w", padx=(0, 20))
        
        # Tema actual
        self.theme_label = ttk.Label(status_grid, textvariable=self.current_theme_var, 
                                    font=("Segoe UI", 9))
        self.theme_label.grid(row=0, column=1, sticky="w")
        
        # Indicadores visuales
        indicators_frame = ttk.Frame(status_grid)
        indicators_frame.grid(row=1, column=0, columnspan=2, sticky="w", pady=(8, 0))
        
        # Brillo
        brillo_frame = ttk.Frame(indicators_frame)
        brillo_frame.pack(side="left", padx=(0, 15))
        
        ttk.Label(brillo_frame, text="💡", font=("Segoe UI", 9)).pack(side="left")
        self.brillo_canvas = tk.Canvas(brillo_frame, width=30, height=8, 
                                      highlightthickness=0, bg="#4a90e2")
        self.brillo_canvas.pack(side="left", padx=(2, 0))
        
        # Volumen
        vol_frame = ttk.Frame(indicators_frame)
        vol_frame.pack(side="left")
        
        ttk.Label(vol_frame, text="🔊", font=("Segoe UI", 9)).pack(side="left")
        self.vol_value = ttk.Label(vol_frame, text="50%", 
                                  font=("Segoe UI", 9, "bold"))
        self.vol_value.pack(side="left", padx=(2, 0))
        
        # Separador
        ttk.Separator(self.main_frame).pack(pady=12, fill="x")
        
        # Panel de navegación principal
        nav_frame = ttk.LabelFrame(self.main_frame, text="🧭 Navegación Principal", padding=15)
        nav_frame.pack(fill="both", expand=True)
        
        # Botones de navegación con mejor estilo
        nav_buttons = [
            ("🏠 Inicio", "#4a90e2", lambda: open_win_home(self)),
            ("📝 Formulario", "#48bb78", lambda: open_win_form(self)),
            ("🎯 Lista de Metas", "#ed8936", lambda: open_win_list(self)),
            ("📅 Calendario", "#9f7aea", lambda: open_win_table(self, 2025, 10)),
            ("⚙️ Ajustes", "#718096", lambda: open_win_canvas(self, apply_settings_callback=self.apply_settings))
        ]
        
        for text, color, command in nav_buttons:
            btn = tk.Button(
                nav_frame,
                text=text,
                command=command,
                bg=color,
                fg='white',
                font=("Segoe UI", 11, "bold"),
                relief="flat",
                bd=0,
                padx=20,
                pady=10,
                cursor="hand2",
                width=18
            )
            
            # Efecto hover simple
            def make_hover(btn, color):
                def on_enter(e):
                    btn.config(bg=self.aumentar_brillo(color, 15))
                def on_leave(e):
                    btn.config(bg=color)
                return on_enter, on_leave
            
            on_enter, on_leave = make_hover(btn, color)
            btn.bind("<Enter>", on_enter)
            btn.bind("<Leave>", on_leave)
            
            btn.pack(pady=5, fill="x")
        
        # Separador final
        ttk.Separator(self.main_frame).pack(pady=12, fill="x")
        
        # Panel de footer
        footer_frame = ttk.Frame(self.main_frame)
        footer_frame.pack(fill="x")
        
        # Botón de salir con estilo diferente
        exit_btn = tk.Button(
            footer_frame,
            text="🚪 Salir de la Aplicación",
            command=self.destroy,
            bg="#f56565",
            fg='white',
            font=("Segoe UI", 10, "bold"),
            relief="flat",
            bd=0,
            padx=20,
            pady=8,
            cursor="hand2"
        )
        
        # Efecto hover para salir
        exit_btn.bind("<Enter>", lambda e: exit_btn.config(bg="#e53e3e"))
        exit_btn.bind("<Leave>", lambda e: exit_btn.config(bg="#f56565"))
        
        exit_btn.pack(side="right")

    def aumentar_brillo(self, hex_color, factor):
        """Aumenta el brillo de un color hex"""
        hex_color = hex_color.lstrip('#')
        r, g, b = int(hex_color[0:2], 16), int(hex_color[2:4], 16), int(hex_color[4:6], 16)
        r = min(255, r + factor)
        g = min(255, g + factor)
        b = min(255, b + factor)
        return f"#{r:02x}{g:02x}{b:02x}"

    def apply_settings(self, settings: dict):
        """Aplica los ajustes desde el panel de configuración"""
        print(f"✅ Aplicando ajustes globales: {settings}")
        
        # Aplicar tema
        if settings.get("modo_noche"):
            self.apply_theme("dark")
        else:
            self.apply_theme("light")
        
        # Aplicar brillo
        new_brillo = settings.get("brillo", 70)
        color_val = int(255 * (new_brillo / 100))
        brillo_color = f"#{color_val:02x}{color_val:02x}{color_val:02x}"
        self.brillo_canvas.config(bg=brillo_color)

        # Aplicar resolución
        new_res = settings.get("resolucion", 50)
        width = int(400 + 3 * new_res) 
        height = int(450 + 2.5 * new_res) 
        self.geometry(f"{width}x{height}")
        
        # Aplicar volumen
        new_vol = settings.get("volumen", 50)
        self.current_volume.set(f"Volumen: {new_vol:.0f}")
        self.vol_value.config(text=f"{new_vol:.0f}%")

def main():
    app = App()
    app.mainloop()

if __name__ == "__main__":
    main()