from tkinter import *
from tkinter import ttk

def calculateur(): 
    root2 = Tk()
    a = float(entryTotal.get())
    b = float(entryUsed.get())
    total = b / a
    ttk.Label(root2, text=f"Disque utilisé à {total*100} %").grid(row=1, column=0)
    root2.mainloop()

root = Tk()
root.title("Disk Manager")
labelTotal = ttk.Label(root,text="Total capacity (Gb)")
entryTotal = ttk.Entry(root)
labelUsed = ttk.Label(root,text="Used capacity (Gb)")
entryUsed = ttk.Entry(root)

button = ttk.Button(root,text="Percent usage", command=calculateur)

labelTotal.grid(row=1, column=0)
entryTotal.grid(row=1, column=1)
labelUsed.grid(row=2, column=0)
entryUsed.grid(row=2, column=1)
button.grid(row=3, column=1)

root.mainloop()