from tkinter import *
def clicked():
    lbl.configure(text="Bye")

window = Tk()
window.title("Button")
window.geometry("500x300")
lbl = Label(window, text="Hello", font=("Arial", 50))
lbl.grid(column = 0, row = 0)

btn=Button(window, text="Кнопочка", bg='black', fg='yellow', command=clicked)
btn.grid(column = 1, row = 0)


window.mainloop()