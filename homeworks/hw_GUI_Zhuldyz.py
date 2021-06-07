from math import pi
from tkinter import *

window = Tk()
def square(r):
    S = pi*r*r
    text = "Площадь круга равна  %s \n " %(S)
    return text
def inserter(value):
    output.delete("0.0", "end")
    output.insert("0.0", value)

def handler():
    try:
        r_val = float(r.get())
        inserter(square(r_val))
    except ValueError:
        inserter("Убедитесь, что вы ввели радиус круга")


window.title("Площадь круга")
window.minsize(350, 250) #устанавливаем минимальный размер окна
window.resizable(width=False, height=False) #выключаем возможность изменять окно
frame = Frame(window)
frame.grid()


r = Entry(frame, width = 5)
r.grid(row = 0, column = 1)
r.configure(font=("Courier", 14, "bold"))

lbl_r = Label(frame, text = "Введи радиус круга: ")
lbl_r.grid(row = 0, column = 0, padx = 10)
lbl_r.configure(font=("Courier", 14, "bold"))

btn = Button(frame, text = "Найти",command = handler)
btn.grid(row = 0, column = 6)
btn.configure(font=("Courier", 14, "italic"))

output = Text(frame, bg="lightgreen", font = "Arial 14", width = 60, height = 20)
output.grid(row = 2, columnspan=8)

window.mainloop()