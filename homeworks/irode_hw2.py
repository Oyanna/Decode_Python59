from math import sqrt
from tkinter import *
window=Tk()
def pl(p, r):
    return p*r**2

def inserter(value):
    output.delete("0.0", "end")
    output.insert("0.0", value)

def handler():
    try:
        p_val = float(p.get())
        r_val = float(r.get())
        inserter(pl(p_val, r_val))
    except ValueError:
        inserter("Убедитесь, что вы ввели числа")

window.title("Площадь круга")
window.minsize(200,150)

p=Entry(window, width=5)
p.grid(row=0, column=0)

lbl1=Label(window, text="*")
lbl1.grid(row=0, column=1)

r=Entry(window, width=5)
r.grid(row=0, column=2)

lbl2=Label(window, text="**2")
lbl2.grid(row=0, column=3)

output = Text(window, bg="pink", font = "Arial 12", width = 50, height = 15)
output.grid(row = 1, columnspan=8)

btn = Button(window, text = "=", command = handler)
btn.grid(row = 0, column = 4)

window.mainloop()

