from tkinter import *
from tkinter.ttk import Radiobutton

def clicked():
    lbl.configure(text=selected.get())


window=Tk()
window.title("Example1")
window.geometry("500x300")

selected = IntVar()

rd1 = Radiobutton(window, text="Первый", value=1, variable=selected)
rd2 = Radiobutton(window, text="Второй", value=7, variable=selected)
rd3 = Radiobutton(window, text="Третий", value=8, variable=selected)

rd1.grid(column=0, row=0)
rd2.grid(column=1, row=0)
rd3.grid(column=2, row=0)

btn = Button(window, text="OK", command=clicked)
btn.grid(column=3, row=0)

lbl = Label(window)
lbl.grid(column=0, row=1)

window.mainloop()
