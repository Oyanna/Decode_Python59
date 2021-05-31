from tkinter import *
from tkinter.ttk import Checkbutton


window = Tk()
window.title("Checkbutton")
window.geometry("500x300")

ch_state = BooleanVar() #InVar()
ch_state.set(True)
ch = Checkbutton(window, text = "Нажмите, если вы с политикой конф", var = ch_state)
ch.grid(column = 0, row = 0)


window.mainloop()
