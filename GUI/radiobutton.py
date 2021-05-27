from tkinter import *
from tkinter.ttk import Checkbutton
def clicked1():
    lbl1.configure(text = "Bye")
def clicked2():
    lbl1.configure(text = "hi")


window = Tk()
window.title("Radiobutton")
window.geometry("500x300")

lbl1 = Label(window, text = "hello")
lbl1.grid(column = 0, row = 1)

rd1 = Radiobutton(window, text ="first", value = 1, command = clicked1)
rd2 = Radiobutton(window, text ="second", value = 2, command = clicked2)
rd3 = Radiobutton(window, text ="third", value = 3)
rd1.grid(column=0, row=0)
rd2.grid(column=1, row=0)
rd3.grid(column=2, row=0)
window.mainloop()