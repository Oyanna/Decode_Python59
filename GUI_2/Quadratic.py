from math import sqrt
from tkinter import *

window = Tk()
def solve(a, b, c):
    d = b*b - 4*a*c
    if d >=0:
        x1 = (-b + sqrt(d))/(2*a)
        x2 = (-b - sqrt(d))/(2*a)
        text = "Dicriminant  %s \n x1 - это %s \n x2 - это %s" %(d,x1,x2)
    else:
        text = "Dicriminant < 0. No solutions"
    return text
def inserter(value):
    output.delete("0.0", "end")
    output.insert("0.0", value)

def handler():
    try:
        a_val = float(a.get())
        b_val = float(b.get())
        c_val = float(c.get())
        inserter(solve(a_val, b_val, c_val))
    except ValueError:
        inserter("Убедитесь, что вы ввели три цифры")


window.title("Quadratic")
window.minsize(350, 250) #устанавливаем минимальный размер окна
window.resizable(width=False, height=False) #выключаем возможность изменять окно
frame = Frame(window)
frame.grid()

a = Entry(frame, width = 3)
a.grid(row = 0, column = 0)

lbl_a = Label(frame, text = "x*x +")
lbl_a.grid(row = 0, column = 1)

b = Entry(frame, width = 3)
b.grid(row = 0, column = 2)

lbl_b = Label(frame, text = "x +")
lbl_b.grid(row = 0, column = 3)


c = Entry(frame, width = 3)
c.grid(row = 0, column = 4)

lbl_c = Label(frame, text = "= 0")
lbl_c.grid(row = 0, column = 5)


btn = Button(frame, text = "Решить", command = handler)
btn.grid(row = 0, column = 6)

output = Text(frame, bg="lightblue", font = "Arial 12", width = 50, height = 15)
output.grid(row = 1, columnspan=8)

window.mainloop()


