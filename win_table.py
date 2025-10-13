import tkinter as tk
from tkinter import ttk, messagebox
from tkcalendar import Calendar
import csv
from pathlib import Path

CSV_PATH = Path(__file__).resolve().parents[1] / "data" / "calendario.csv"

def cargar_eventos():
    eventos = {}
    if CSV_PATH.exists():
        with open(CSV_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                fecha = row["fecha"]  # formato: 'YYYY-MM-DD'
                titulo = row["titulo"]
                if fecha in eventos:
                    eventos[fecha].append(titulo)
                else:
                    eventos[fecha] = [titulo]
    return eventos

def open_win_table(parent: tk.Tk, year: int, month: int):
    win = tk.Toplevel(parent)
    win.title(f"Calendario: {year}-{month:02}")
    win.geometry("400x400")

    eventos = cargar_eventos()

    # Crear calendario mostrando el mes y año deseados
    cal = Calendar(win, selectmode="day", year=year, month=month, day=1, date_pattern='yyyy-mm-dd')
    cal.pack(padx=10, pady=10, fill="both", expand=True)

    # Label para mostrar eventos del día seleccionado
    eventos_label = tk.Label(win, text="Selecciona una fecha para ver eventos", justify="left")
    eventos_label.pack(padx=10, pady=10, fill="both", expand=True)

    def mostrar_eventos(event):
        fecha_sel = cal.get_date()  # string 'YYYY-MM-DD'
        lista_eventos = eventos.get(fecha_sel, [])
        if lista_eventos:
            texto = f"Eventos para {fecha_sel}:\n" + "\n".join(f"• {e}" for e in lista_eventos)
        else:
            texto = f"No hay eventos para {fecha_sel}."
        eventos_label.config(text=texto)

    # Vincular selección de fecha para mostrar eventos
    cal.bind("<<CalendarSelected>>", mostrar_eventos)

    # Botón cerrar
    ttk.Button(win, text="Cerrar", command=win.destroy).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    root.withdraw()  # ocultar ventana principal
    open_win_table(root, 2025, 10)
    root.mainloop()
_
