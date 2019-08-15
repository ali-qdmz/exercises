from tkinter import *
root = Tk()
logo = PhotoImage(file="ravandi.gif")
W1 = Label(root, image=logo).pack(side="right")
explanation = "matne tasvir"
W2 = Label(root,justify=LEFT,padx = 10, text=explanation).pack(side="left")
root.mainloop()
