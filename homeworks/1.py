from tkinter import *
from tkinter.ttk import Combobox


def solver(a):
    a1=int(a)
    oper1 = operator1.get()
    oper2 = operator2.get()
    res=0
    if oper1=="Площадь" and oper2=="Круг":
        res=3.14*a1**2
    elif oper1=="Площадь" and oper2=="Квадрат":
        res=a1**2
    elif oper1=="Периметр" and oper2=="Квадрат":
        res=a1*4
    elif oper1=="Периметр" and oper2=="Круг":
        res=2*3.14*a1
    res="Ответ:" + str(res)
    return res

def inserter(value):
    output.delete("0.0", "end")
    output.insert("0.0", value)

def handler():
    try:
        a_val = int(inp.get())
        inserter(solver(a_val))
    except ValueError:
        inserter("Ошибка")

def clear(event):
    caller=event.widget
    caller.delete("0", "end")

window=Tk()
window.title("Calculator")
window.minsize(500,350)


inp=Entry(window,width=5)
inp.bind("<FocusIn>", clear)
inp.grid(row=0, column=0)

operator1=Combobox(window, width=15)
operator1['values']=("Площадь", "Периметр")
operator1.current(0)
operator1.grid(row=0, column=1)

operator2=Combobox(window, width=10)
operator2['values']=("Круг", "Квадрат")
operator2.current(0)
operator2.grid(row=0, column=2)

output = Text(window, bg="pink", fg='white',  font = "Arial 20", width=25, height=10)
output.grid(row=1, columnspan=8)

btn=Button(window, text="=", command=handler)
btn.grid(row=0, column=3)


window.mainloop()

