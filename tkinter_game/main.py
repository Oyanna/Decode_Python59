from tkinter import *
from random import *

def f1():
    global count
    c = 1
    count=count-c
    if count <= 0:
        palochki.config(text="Вы проиграли!", fg="red")
    else:
        palochki.config(text=count * " | ")
def f2():
    global count
    c = 2
    count=count-c
    if count<=0:
        palochki.config(text="Вы проиграли!", fg="red")
    else:
        palochki.config(text=count*" | ")
def f3():
    global count
    c = 3
    count = count-c
    if count<=0:
        palochki.config(text="Вы проиграли!", fg="red")
    else:
        palochki.config(text=count * " | ")

def pc():
    global count
    c = randint(1, 3)
    if count == 4:
        c = 3
    elif count == 3:
        c = 2
    elif count == 2:
        c = 1
    count = count - c
    if count <= 0:
        palochki.config(text="Вы выиграли!")
    else:
        palochki.config(text = count* " | ")



count=20
window = Tk()
window.geometry("500x200")
window.resizable(0,0)
window.title("Палочки")

text1 = Label(window, text="Сколько палочек вам нужно?")
text1.config(font=("Arial", 20, 'bold'))
text1.grid(row=0, column=4)
btn1 = Button(window, text="1", command=f1)
btn1.grid(row=1, column=2, columnspan=2)
btn2 = Button(window, text="2", command=f2)
btn2.grid(row=1, column=4, columnspan=2)
lbl1 = Label(window, text="       ").grid(row=2, column=4)
btn3 = Button(window, text="3", command=f3)
btn3.grid(row=1, column=6, columnspan=2)
palochki = Label(window, text=count*" | ", fg="green")
palochki.config(font=("Arial", 30, 'bold'))
palochki.grid(row=2, column=1, columnspan=8)

btn_pc = Button(window, text="Ход компьютера", width=20, command=pc)
btn_pc.grid(row=3, column=3, columnspan=4)

window.mainloop()

