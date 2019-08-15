from tkinter import *

root = Tk()

data = IntVar()

entry = Entry()
entry.grid()

def click(event):
    # Get the number, add 1 to it, and then print it
    print (float(entry.get()) + 1)

# Bind the entrybox to the Return key
entry.bind("<S>", click)

root.mainloop()
