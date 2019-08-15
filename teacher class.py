class teacher:
    def __init__(self,i="",f="",l="",h=0,p=0):
        self.id = i
        self.firstname = f
        self.lastname = l
        self.hour = h
        self.payperhour = p
    def getID(self):
        return self.id
    def setID(self,value):
        self.id = value
    def setFirstName(self,value):
        self.firstname = value
    def setLastName(self,value):
        self.lastname = value
    def getLastName(self,value):
        return self.getlastname
    def getFirstName(self,value):
        return self.firstname
    def getHour(self):
        return self.hour
    def setHour(self,value):
        if value > 0:
            self.hour = value
        else:
            self.hour = 0
    def payperonhour(self):
        return self.payperhour
    def setpayperhour(self,value):
        if value > 0:
            self.payperhour = value
        else:
            self.payperhour = 0
    def payment(self):
        return str((float(self.hour) * float(self.payperhour)))
    def __str__(self):
        return str(self.id) + "   " + str(self.firstname) + "     " + str(self.lastname) + "     " + str(self.hour) + "    " + str(self.payperhour) + "    "+ str(self.payment())

class Stack:
    def __init__(self):
            self.items = []
    def push(self,item):
          self.items.append(item)
    def pop(self):
             return print(self.items.pop())
    def isEmpty(self):
           return (self.items == [])

My_Stack = Stack()

from tkinter import *

def show_entry_fields():
    
    x = teacher(e1.get(),e2.get(),e3.get(),e4.get(),e5.get())
    My_Stack.push(x)
    print(x)

    



master = Tk()
master.geometry("500x500")
Label(master, text="First Name").grid(row=0)
Label(master, text="Last Name").grid(row=1)
Label(master, text="Id").grid(row=2)
Label(master, text="teach hour").grid(row=3)
Label(master, text="pay per hour").grid(row=4)

e1 = Entry(master)
e2 = Entry(master)
e3 = Entry(master)
e4 = Entry(master)
e5 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)

Button(master, text='Quit', command=master.destroy).grid(row=5, column=0)

Button(master, text='Show', command=show_entry_fields).grid(row=5, column=1)

mainloop( )
    
        
    
