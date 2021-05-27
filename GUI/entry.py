from tkinter import *
def clicked():
    res = txt.get()
    lbl.configure(text=res)
    #print(res) - проверка получили ли мы данные или нет

window = Tk()
window.title("Our first GUI")
window.geometry("500x300")
lbl = Label(window, text="Hello", font=("Arial", 50))
lbl.grid(column = 0, row = 0)

btn=Button(window, text="Кнопочка", bg='black', fg='yellow', command=clicked)
btn.grid(column = 1, row = 0)

txt = Entry(window, width=15)
txt.grid(column = 2, row = 0)
txt.focus()

window.mainloop()