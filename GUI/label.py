from tkinter import *
window = Tk()
window.title("Привет, мир!")
lbl1 = Label(window, text = "hello")
lbl1.grid(column = 0, row = 0)
lbl2 = Label(window, text = "hello")
lbl2.grid(column = 1, row = 0)
lbl3 = Label(window, text = "hello")
lbl3.grid(column = 2, row = 0)

window.mainloop()