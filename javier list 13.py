import tkinter as tk
from tkinter import ttk, messagebox

def open_win_list(parent: tk.Tk):
    win = tk.Toplevel(parent)
    win.title("Metas")
    win.geometry("600x500")

    frm = ttk.Frame(win, padding=12)
    frm.pack(fill="both", expand=True)

    # Lista de tareas pendientes
    lb = tk.Listbox(frm, height=10)
    lb.grid(row=1, column=0, rowspan=4, sticky="nsew", padx=(0, 8))
    frm.columnconfigure(0, weight=1)
    frm.rowconfigure(0, weight=1)

    # Lista de tareas terminadas
    lb_done = tk.Listbox(frm, height=6)
    lb_done.grid(row=6, column=0, columnspan=2, sticky="nsew", pady=(10, 0))
    lbl_done = tk.Label(frm, text="Tareas Terminadas", font=("Segoe UI", 10))
    lbl_done.grid(row=5, column=0, columnspan=2, pady=(10, 0), sticky="w")

    ent_item = ttk.Entry(frm)
    ent_item.grid(row=0, column=1, sticky="ew")
    lbl_titulo = tk.Label(frm, text="Lista de Metas", font=("Segoe UI", 12))
    lbl_titulo.grid(row=0, column=0, columnspan=1, pady=(0,10), sticky="n")

    def agregar():
        v = ent_item.get().strip()
        if v:
            lb.insert("end", v)
            ent_item.delete(0, "end")
        else:
            messagebox.showwarning("Aviso", "Escribe un texto para agregar.")

    def eliminar():
        sel = lb.curselection()
        if sel:
            lb.delete(sel[0])

    def terminar_tarea():
        sel = lb.curselection()
        if sel:
            tarea = lb.get(sel[0])
            lb.delete(sel[0])
            lb_done.insert("end", tarea)

    def limpiar():
        lb.delete(0, "end")

    def limpiar_terminadas():
        lb_done.delete(0, "end")

    ttk.Button(frm, text="Agregar", command=agregar).grid(row=1, column=1, sticky="ew", pady=4)
    ttk.Button(frm, text="Eliminar seleccionado", command=eliminar).grid(row=2, column=1, sticky="ew", pady=4)
    ttk.Button(frm, text="Terminar Tarea", command=terminar_tarea).grid(row=3, column=1, sticky="ew", pady=4)
    ttk.Button(frm, text="Limpiar", command=limpiar).grid(row=4, column=1, sticky="ew", pady=4)
    ttk.Button(frm, text="Limpiar Terminadas", command=limpiar_terminadas).grid(row=7, column=0, columnspan=2, sticky="ew", pady=10)
    ttk.Button(frm, text="Cerrar", command=win.destroy).grid(row=8, column=0, columnspan=2, pady=10, sticky="e")
