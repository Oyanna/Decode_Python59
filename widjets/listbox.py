from tkinter import *
from tkinter.ttk import *
class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.master.title("Список")
        self.pack(fill=BOTH, expand=1)
        classes = [
            'алгебра', 'геометрия', 'физика', 'информатика'
        ]

        lb = Listbox(self)
        for i in classes:
            lb.insert(END, i)
        lb.bind("<<ListboxSelect>>", self.onSelect)
        lb.pack(pady=10)
        self.var=StringVar()
        self.label=Label(self, text=0, textvariable=self.var)
        self.label.pack()

    def onSelect(self, val):
        sender=val.widget
        idx=sender.curselection()
        value=sender.get(idx)
        self.var.set(value)



def main():
    window=Tk()
    ex = Example()
    window.geometry("300x150")
    window.mainloop()

if __name__ == '__main__':
    main()

