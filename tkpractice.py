from tkinter import *
win = Tk() # Create the root (base) window 
win.geometry("300x200+10+20")
w = Label(win, text="Hello, this is a trial window!") # Create a label with words
w.pack() # Put the label into the window
b = Button(win, text = "Submit")  
  
b.pack()

win.mainloop()# Start the event loop