import tkinter as tk
window=tk.Tk()
frame1=tk.Frame(master=window, height=300, bg="lightblue")
frame1.pack(fill=tk.X)
frame2=tk.Frame(master=window, height=200, bg="yellow")
frame2.pack(fill=tk.X)
frame3=tk.Frame(master=window, height=100, bg="purple")
frame3.pack(fill=tk.X)
window.mainloop()