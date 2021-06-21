from tkinter import Tk, Frame, Menu

class Example(Frame):
    def __init__(self):
        super().__init__()
        self.initUI()
    def initUI(self):
        self.master.title("SubMenu")

        menubar=Menu(self.master)
        self.master.config(menu=menubar)

        fileMenu=Menu(menubar)

        submenu=Menu(self.master)
        submenu.add_command(label="Новый источник");
        submenu.add_command(label="Закладки")
        submenu.add_command(label="Версии")

        fileMenu.add_cascade(label="Импортировать", menu=submenu, underline=0)
        fileMenu.add_separator()
        fileMenu.add_command(label="Выход", underline=0, command=self.onExit)
        menubar.add_cascade(label="Файл", underline=0, menu=fileMenu)


    def onExit(self):
        self.quit()


def main():
    window=Tk()
    window.geometry("300x150")
    ex = Example()
    window.mainloop()

if __name__ == '__main__':
    main()