from tkinter import *
from tkinter.ttk import *

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.master.title("Шкала с ползунком")
        self.style=Style()
        self.style.theme_use("default")

        self.pack(fill=BOTH, expand=1)

        scale=Scale(self, from_=0, to=100, command=self.onScale)
        scale.pack(side=LEFT, padx=15)
        self.var=IntVar()
        self.label=Label(self, text=0, textvariable=self.var)
        self.label.pack(side=LEFT)


    def onScale(self, val):
        a = int(float(val))
        self.var.set(a)


def main():
    window=Tk()
    ex = Example()
    window.geometry("300x150")
    window.mainloop()

if __name__ == '__main__':
    main()



