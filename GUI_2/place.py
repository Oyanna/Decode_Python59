import tkinter as tk

window=tk.Tk()
window.minsize(300, 300)
frame=tk.Frame(master=window, width=300, height=300)
frame.pack()

lbl1=tk.Label(master=frame, text="Я на (0,0)", bg="red")
lbl1.place(x=0, y=0)

lbl2=tk.Label(master=frame, text="Я на (200,200)", bg="blue")
lbl2.place(x=200, y=200)
window.mainloop()
