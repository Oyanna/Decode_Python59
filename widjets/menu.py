from tkinter import Tk, Frame, Menu

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

def main():
    window=Tk()
    window.geometry("300x150")
    ex = Example()
    window.mainloop()

if __name__ == '__main__':
    main()