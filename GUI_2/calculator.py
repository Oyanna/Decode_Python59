from tkinter import *
from tkinter.ttk import Combobox

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.master.title("Simple Menu")
        menubar=Menu(self.master)
        self.master.config(menu=menubar)
        fileMenu=Menu(menubar)
        fileMenu.add_command(label="New file")
        fileMenu.add_command(label="Exit", command=self.onExit)
        menubar.add_cascade(label="Подробнее", menu=fileMenu)
    def onExit(self):
        self.quit()

def calc(inp1, inp2):
    a = int(inp1)
    b = int(inp2)
    oper = operator.get()
    res = 0
    if oper == '+':
        res = a+b
    elif oper == '-':
        res = a-b
    elif oper == '*':
        res = a*b
    elif oper == '/' and b != 0:
        res = a/b
    elif oper == '/' and b == 0:
        return ("На ноль делить нельзя!")
    res = "Результат равен " + str(res)
    return res


def inserter(value):
    output.delete("0.0", "end")
    output.insert("0.0", value)

def handler():
    try:
        inp1_val = int(inp1.get())
        inp2_val = int(inp2.get())
        inserter(calc(inp1_val, inp2_val))
    except ValueError:
        inserter("Убедитесь, что вы ввели оба аргумента")
def clear(event):
    caller=event.widget
    caller.delete("0", "end")


window = Tk()
window.title("Calculator")
ex = Example()
window.minsize(100, 100)
window.resizable(width=False, height=False)

inp1=Entry(window, width=10)
inp1.bind("<FocusIn>", clear)
inp1.grid(row=0, column=0)

inp2=Entry(window, width=10)
inp2.bind("<FocusIn>", clear)
inp2.grid(row=0, column=2)

operator=Combobox(window, width=10)
operator['values']=('+', '-', '*', '/')
operator.current(0)
operator.grid(row=0, column=1)

output = Text(window, bg="lightblue", font = "Arial 25", width=25, height=10)
output.grid(row=1, columnspan=8)

btn=Button(window, text="=", command=handler)
btn.grid(row=0, column=3)


window.mainloop()





