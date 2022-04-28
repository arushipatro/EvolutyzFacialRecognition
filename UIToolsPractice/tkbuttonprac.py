import tkinter
from tkinter import *
from tkinter import messagebox

top = Tk()
top.geometry("300x150")
def click():
    messagebox.showinfo("Hello", "Green Button clicked")
a = Button(top, text="yellow", activeforeground="yellow", activebackground="orange", pady=10)
b = Button(top, text="Blue", activeforeground="blue", activebackground="orange", pady=10)
# adding click function to the below button
c = Button(top, text="Green", command=click, activeforeground = "green", activebackground="orange", pady=10)
d = Button(top, text="red", activeforeground="yellow", activebackground="orange", pady=10)

a.pack(side = LEFT)
b.pack(side = RIGHT)
c.pack(side = TOP)
d.pack(side = BOTTOM)
top.mainloop()

