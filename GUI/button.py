from tkinter import *
window = Tk()
window.title("Button")
window.geometry("500x300")

btn=Button(window, text="Кнопочка", bg='black', fg='yellow')
btn.grid(column = 0, row = 0)

window.mainloop()