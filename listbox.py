from tkinter import *
master = Tk()
listbox = Listbox(master)
listbox.pack()
listbox.insert(END,'new text')
for item in ['first text','second text','third text','forth text']:
    listbox.insert(END,'new text')
mainloop()
