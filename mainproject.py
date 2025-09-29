import tkinter as tk
from tkinter import ttk, messagebox

# Aquí podrías importar o definir las funciones que abrirían cada sección:
# from app.win_calendar import open_win_calendar
# from app.win_project import open_win_project
# ... etc

def on_open_selected(root, listbox):
    selection = listbox.curselection()
    if not selection:
        messagebox.showwarning("Aviso", "Selecciona un ítem de la lista")
        return
    
    item = listbox.get(selection[0])
    # Aquí podrías lanzar la ventana o funcionalidad según el ítem seleccionado
    # Ejemplo básico con mensaje:
    messagebox.showinfo("Seleccionado", f"Has abierto: {item}")

def main():
    root = tk.Tk()
    root.title("Proyecto Integrador - MVP")
    root.geometry("420x340")

    frame = ttk.Frame(root, padding=16)
    frame.pack(fill="both", expand=True)

    ttk.Label(frame, text="Aplicación Demo (tkinter)", font=("Segoe UI", 12, "bold")).pack(pady=(0, 12))

    items = ["calendar", "Project", "data", "goal tracker", "meetings", "Announcements"]

    listbox = tk.Listbox(frame, height=8)
    for item in items:
        listbox.insert(tk.END, item)
    listbox.pack(pady=8, fill="x")

    ttk.Button(frame, text="Abrir seleccionado", command=lambda: on_open_selected(root, listbox)).pack(pady=4, fill="x")

    ttk.Separator(frame).pack(pady=6, fill="x")
    ttk.Button(frame, text="Salir", command=root.destroy).pack(pady=6)

    root.mainloop()

if __name__ == "__main__":
    main()
