from tkinter import *
from tkinter.ttk import Checkbutton
from tkinter.ttk import Combobox
def clicked():
    btn.configure(text="$500")
    btn1.configure(text="$750")
window=Tk()
window.title("Be Your Travel guide")
window.geometry("600x500")
lbl1=Label(window, text="HELLO and WELCOME to everyone!",bg="yellow", fg="blue", font=("Broadway, 15"))
lbl1.grid(column=0, row=1)
lbl2=Label(window, text="If you want to go travel, you can choose one option below, so you can know price for travel guide.", font=("Broadway, 10"))
lbl2.grid(column=0, row=2)

btn=Button(window, text="One person", bg="yellow", fg="blue", command=clicked)
btn.grid(column=0, row=3)

btn1=Button(window, text="Two people", bg="yellow", fg="blue", command=clicked)
btn1.grid(column=1,row=3)

lbl3=Label(window, text="Now you can choose one of them and contact me!", font=("Broadway, 10"))
lbl3.grid(column=0, row=4)

combo=Combobox(window)
combo["values"]=(1, 2)
combo.current(0)
combo.grid(column=0, row=5)

lbl4=Label(window, text="Phone number: 867890456", bg="light green", fg="black", font=("Broadway, 10"))
lbl4.grid(column=0, row=6)

lbl5=Label(window, text="You also can send your contact to my email and I will contact you as soon as possible",  font=("Broadway, 10"))
lbl5.grid(column=0, row=7)

lbl6=Label(window, text="Email: yelinna@gmail.com",bg="light green", fg="black",  font=("Broadway, 10"))
lbl6.grid(column=0, row=8)

aya=BooleanVar()
aya.set(False)
ch=Checkbutton(window,text="Click if you are interested", var=aya)
ch.grid(column=0, row=9)

window.mainloop()
