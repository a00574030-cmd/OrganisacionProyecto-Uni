import tkinter as tk
from tkinter import ttk, messagebox
import requests
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


def fetch_data():
    """
    Conecta con la API de Open-Meteo y obtiene datos horarios
    de Chilpancingo (últimas 24 horas).
    Devuelve: horas, temperaturas, humedad, viento.
    """
    try:
        url = (
            "https://api.open-meteo.com/v1/forecast"
            "?latitude=17.55&longitude=-99.50"  # Chilpancingo
            "&hourly=temperature_2m,relativehumidity_2m,windspeed_10m"
            "&past_days=1"
            "&timezone=auto"
        )
        response = requests.get(url, timeout=15)
        response.raise_for_status()
        data = response.json()

        horas = data["hourly"]["time"]
        temperaturas = data["hourly"]["temperature_2m"]
        humedad = data["hourly"]["relativehumidity_2m"]
        viento = data["hourly"]["windspeed_10m"]

        return horas, temperaturas, humedad, viento
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron obtener los datos:\n{e}")
        return [], [], [], []


def create_line_chart(horas, valores, titulo, ylabel):
    """Gráfica de línea personalizada."""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.plot(
        horas,
        valores,
        linestyle="-",
        marker="s",         # marcador cuadrado
        markersize=4,
        linewidth=1.5,      # grosor de línea
        alpha=0.8           # transparencia
    )
    ax.set_title(titulo)
    ax.set_xlabel("Hora")
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, linestyle="--", alpha=.5)  # rejilla
    fig.tight_layout()
    return fig


def create_bar_chart(horas, valores, titulo, ylabel):
    """Gráfica de barras personalizada."""
    fig, ax = plt.subplots(figsize=(6, 3))
    ax.bar(horas, valores, alpha=0.7)
    ax.set_title(titulo)
    ax.set_xlabel("Hora")
    ax.set_ylabel(ylabel)
    ax.tick_params(axis="x", rotation=45)
    ax.grid(True, linestyle="--", alpha=.5)
    fig.tight_layout()
    return fig


def mostrar_graficas(frm, horas, temps, humedad, viento):
    """Inserta las gráficas en el frame de tkinter."""

    # Temperatura
    fig1 = create_line_chart(horas, temps, "Temperatura en Chilpancingo", "°C")
    canvas1 = FigureCanvasTkAgg(fig1, master=frm)
    canvas1.draw()
    canvas1.get_tk_widget().pack(pady=10, fill="x")

    # Humedad relativa
    fig2 = create_line_chart(horas, humedad, "Humedad relativa en Chilpancingo", "%")
    canvas2 = FigureCanvasTkAgg(fig2, master=frm)
    canvas2.draw()
    canvas2.get_tk_widget().pack(pady=10, fill="x")

    # Viento
    fig3 = create_bar_chart(horas, viento, "Velocidad del viento en Chilpancingo", "km/h")
    canvas3 = FigureCanvasTkAgg(fig3, master=frm)
    canvas3.draw()
    canvas3.get_tk_widget().pack(pady=10, fill="x")


def open_win_canvas(parent: tk.Tk):
    """Crea ventana secundaria con gráficas de la API."""
    win = tk.Toplevel(parent)
    win.title("Clima en Chilpancingo - Open-Meteo")
    win.geometry("960x1200")

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    def cargar():
        horas, temps, humedad, viento = fetch_data()
        if horas:
            mostrar_graficas(frm, horas, temps, humedad, viento)

    ttk.Button(frm, text="Cargar y mostrar gráficas", command=cargar).pack(pady=10)


# Para pruebas independientes
if __name__ == "__main__":
    root = tk.Tk()
    root.title("Prueba win_canvas - Chilpancingo")
    ttk.Button(root, text="Abrir ventana Canvas", command=lambda: open_win_canvas(root)).pack(pady=20)
    root.mainloop()
