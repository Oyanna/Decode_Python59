from tkinter import *
window = Tk()
window.title("Привет, мир!")
window.geometry("500x300")
window.resizable(width=False, height=False)

lbl1 = Label(window, text = "hello", font=("Arial", 50))
lbl1.grid(column = 0, row = 0)
lbl2 = Label(window, text = "hello", font=("Arial Bold", 50))
lbl2.grid(column = 0, row = 1)
lbl3 = Label(window, text = "hello")
lbl3.grid(column = 0, row = 2)

window.mainloop()