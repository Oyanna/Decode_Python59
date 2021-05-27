from tkinter import *
from tkinter.ttk import Combobox

window = Tk()
window.title("Combobox")
window.geometry("500x300")

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5)
combo.current(0)
combo.grid(column = 0, row = 0)
window.mainloop()