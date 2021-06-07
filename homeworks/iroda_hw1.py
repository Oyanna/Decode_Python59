from tkinter import *
def clicked1():
    red.configure(text="Красный")

def clicked2():
    orange.configure(text="Оранжевый")
def clicked3():
    yellow.configure(text="Желтый")
def clicked4():
    green.configure(text="Зеленый")
def clicked5():
    light_blue.configure(text="Голубой")
def clicked6():
    blue.configure(text="Синий")
def clicked7():
    purple.configure(text="Фиолетовый")

window=Tk()
window.title("Color of Rainbow")
window.geometry("700x490")
window.minsize(350,150)

red=Button(window, text="Red", bg="red", fg="white", font=("Arial", 10), width=10, height=1, command=clicked1)
red.grid(column=0, row=1)

orange=Button(window, text="Orange", bg="orange", fg="black", font=("Arial", 10), width=10, height=1, command=clicked2)
orange.grid(column=1, row=2)

yellow=Button(window, text="Yellow", bg="yellow", fg="black", font=("Arial", 10), width=10, height=1, command=clicked3)
yellow.grid(column=2, row=3)

green=Button(window, text="Green", bg="green", fg="white", font=("Arial", 10), width=10, height=1,command=clicked4)
green.grid(column=3, row=4)

light_blue=Button(window, text="Light Blue", bg="light blue", fg="black", font=("Arial", 10), width=10, height=1, command=clicked5)
light_blue.grid(column=4, row=5)

blue=Button(window, text="Blue", bg="blue", fg="white", font=("Arial", 10), width=10, height=1, command=clicked6)
blue.grid(column=5, row=6)

purple=Button(window, text="Purple", bg="purple", fg="white", font=("Arial", 10), width=10, height=1, command=clicked7)
blue.grid(column=6, row=7)



window.mainloop()
