from tkinter import *
from tkinter import scrolledtext

window=Tk()
window.title("ScrolledText")
window.geometry("500x300")

txt = scrolledtext.ScrolledText(window, width=30, height=10)
txt.grid(column=0, row=0)

window.mainloop()