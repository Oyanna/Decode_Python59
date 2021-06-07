import tkinter as tk
window=tk.Tk()
frame1=tk.Frame(master=window, width=300, height=300, bg="lightblue")
frame1.pack()
frame2=tk.Frame(master=window, width=200, height=200, bg="yellow")
frame2.pack()
frame3=tk.Frame(master=window, width=100, height=100, bg="purple")
frame3.pack()
window.mainloop()