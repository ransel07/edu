import tkinter as tk
from tkinter import ttk

<<<<<<< HEAD
root = tk.Tk()
root.config(width=300, height=200)
root.title("Boton")

boton = ttk.Button(text="Presiona aqui")
boton.place(x=50, y=50)

root.mainloop()
=======

class Calculadora:
    def __init__(self, num, num2):
        self.num = num
        self.num2 = num2
    
    def sum(self):
        result = self.num + self.num2
        return result
    def rest(self):
        result = self.num - self.num2
        return result
    def mult(self):
        result = self.num * self.num2
        return result
    def div(self):
        result = self.num / self.num2
        return result
    
parameter = Calculadora(3,2)


root = tk.Tk()
root.config(width=300, height=400)
root.title("Boton")

button_sum = ttk.Button(text="+")
button_rest = ttk.Button(text="-")
button_mult = ttk.Button(text="x")
button_div = ttk.Button(text="/")
button_sum.place(x=100, y=60)
button_rest.place(x=50, y=100)
button_mult.place(x=100, y=60)
button_div.place(x=100, y=60)

button_sum.pack()
button_rest.pack()
button_mult.pack()
button_div.pack()

def tock():   
    print (parameter.sum(), parameter.rest(), parameter.mult(), parameter.div())

button_sum.bind("<Button-1>" ,tock())


root.mainloop()


>>>>>>> refs/remotes/origin/master
