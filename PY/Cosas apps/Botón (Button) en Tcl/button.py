import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.config(width=300, height=200)
root.title("Boton")

boton = ttk.Button(text="Presiona aqui")
boton.place(x=50, y=50)

root.mainloop()