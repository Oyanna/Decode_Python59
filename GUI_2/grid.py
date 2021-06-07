import tkinter as tk

window=tk.Tk()

for i in range(3):
    window.columnconfigure(i, weight=10, minsize=50)
    window.rowconfigure(i, weight=10, minsize=50 )
    for j in range(3):
        frame=tk.Frame(
        master=window,
        relief=tk.SUNKEN,
        borderwidth=3
        )
        frame.grid(row=i, column=j, padx=15, pady=15)
        lbl=tk.Label(master=frame, text=f"row {i} \nColumn {j}")
        lbl.pack(padx=15, pady=15)
window.mainloop()