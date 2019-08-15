from tkinter import*
root = Tk()

v = IntVar()
Label(root,text="chose one",justify = LEFT,padx = 20).pack()
Radiobutton(root,text="Python",padx = 20, variable=v,value=1).pack(anchor=W)
Radiobutton(root,text="php",padx = 20,variable=v,value=2).pack(anchor=W)
mainloop()
