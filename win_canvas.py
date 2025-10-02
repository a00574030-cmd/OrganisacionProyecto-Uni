import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def fetch_data():
    """
    Conecta con la API de Open-Meteo y obtiene humedad y viento horario
    de Yucatán (últimas 24 horas).
    Devuelve tres listas: horas, humedad y viento.
    """
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=20.97&longitude=-89.62"
            "&hourly=relativehumidity_2m,windspeed_10m"
            "&past_days=1"
            "&timezone=auto"
        )
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        horas = data["hourly"]["time"]
        humedad = data["hourly"]["relativehumidity_2m"]
        viento = data["hourly"]["windspeed_10m"]

        return horas, humedad, viento
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron obtener los datos:\n{e}")
        return [], [], []


def create_line_chart(horas, datos, ylabel, titulo):
    """Gráfica de línea con mejoras visuales."""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(
        horas,
        datos,
        linestyle="-",
        marker="s",        # marcador cuadrado
        markersize=4,
        linewidth=2,       # grosor de línea
        alpha=0.7          # transparencia
    )
    ax.set_title(titulo)
    ax.set_xlabel("Hora")
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, linestyle="--", alpha=0.5)  # agregar rejilla
    fig.tight_layout()
    return fig


def create_bar_chart(horas, datos, ylabel, titulo):
    """Gráfica de barras con mejoras visuales."""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(horas, datos, alpha=0.7)
    ax.set_title(titulo)
    ax.set_xlabel("Hora")
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, linestyle="--", alpha=0.5)
    fig.tight_layout()
    return fig


def mostrar_graficas(frm, horas, humedad, viento):
    """Inserta gráficas en el frame de la ventana tkinter."""
    # Humedad - Línea
    fig1 = create_line_chart(horas, humedad, "% Humedad", "Humedad en Yucatán (línea)")
    canvas1 = FigureCanvasTkAgg(fig1, master=frm)
    canvas1.draw()
    canvas1.get_tk_widget().pack(pady=10, fill="x")

    # Viento - Barras
    fig2 = create_bar_chart(horas, viento, "km/h", "Velocidad del viento en Yucatán (barras)")
    canvas2 = FigureCanvasTkAgg(fig2, master=frm)
    canvas2.draw()
    canvas2.get_tk_widget().pack(pady=10, fill="x")


def open_win_canvas(parent: tk.Tk):
    """Crea la ventana secundaria con gráficas de la API."""
    win = tk.Toplevel(parent)
    win.title("Canvas con API (Open-Meteo) y gráficas")
    win.geometry("960x1000")

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    # Botón para cargar datos y graficar
    def cargar():
        horas, humedad, viento = fetch_data()
        if horas and humedad and viento:
            mostrar_graficas(frm, horas, humedad, viento)

    ttk.Button(frm, text="Cargar y mostrar gráficas", command=cargar).pack(pady=10)


# Para pruebas independientes
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prueba win_canvas")
    ttk.Button(root, text="Abrir ventana Canvas", command=lambda: open_win_canvas(root)).pack(pady=20)
    root.mainloop()
