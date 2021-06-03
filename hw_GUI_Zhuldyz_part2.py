from tkinter import *
def clicked(color):
       window["bg"]=color
       lbl.configure(text=window["bg"])


window = Tk()
window.title("Цвет окна")
window.minsize(700, 400) #устанавливаем минимальный размер окна
window.resizable(width=False, height=False) #выключаем возможность изменять окно

btn_1 = Button(window, text="Каждый", padx="20", pady="8", font="14")
btn_1.grid(column=0,row=0)
btn_1.config(command=lambda: clicked("red"))
btn_2 = Button(window, text="Охотник", padx="20", pady="8", font="14")
btn_2.grid(column=1,row=1)
btn_2.config(command=lambda: clicked("orange"))
btn_3 = Button(window, text="Желает", padx="20", pady="8", font="14")
btn_3.grid(column=2,row=2)
btn_3.config(command=lambda: clicked("yellow"))
btn_4 = Button(window, text="Знать", padx="20", pady="8", font="14")
btn_4.grid(column=3,row=3)
btn_4.config(command=lambda: clicked("green"))
btn_5 = Button(window, text="Где", padx="20", pady="8", font="14")
btn_5.grid(column=4,row=4)
btn_5.config(command=lambda: clicked("light blue"))
btn_6 = Button(window, text="Сидит", padx="20", pady="8", font="14")
btn_6.grid(column=5,row=5)
btn_6.config(command=lambda: clicked("blue"))
btn_7 = Button(window, text="Фазан", padx="20", pady="8", font="14")
btn_7.grid(column=6,row=6)
btn_7.config(command=lambda: clicked("violet"))
lbl = Label(window, font="Arial 20", width=15, bg="white", text="Hello")
lbl.grid(column=0, row=3)

window.mainloop()