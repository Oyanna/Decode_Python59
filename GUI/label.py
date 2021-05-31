from tkinter import *
window = Tk()
window.title("Привет, мир!")
lbl1 = Label(window, text = "hello")
lbl1.grid(column = 0, row = 0)
lbl2 = Label(window, text = "hello")
lbl2.grid(column = 0, row = 1)
lbl3 = Label(window, text = "hello")
lbl3.grid(column = 0, row = 2)

window.mainloop()