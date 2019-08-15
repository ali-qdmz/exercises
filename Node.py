class Node:
    def __init__(self, cargo=None, next=None):
        self.cargo = cargo
        self.next = next
    def __str__(self):
         return str(self.cargo)

def printList(node):
    while node:
          
          print(str(node), end="")
          node = node.next
    
def printBackward(list):
    if list == None: return
    head = list
    tail = list.next
    printBackward(tail)
    print(head,)


def removeSecond(list):
    if list == None: return
    first = list
    second = list.next
# make the first node refer to the third
    first.next = second.next
# separate the second node from the rest of the list
    second.next = None
    return second



def removeSecond(list):
    if list == None: return
    first = list
    second = list.next
# make the first node refer to the third
    first.next = second.next
# separate the second node from the rest of the list
    second.next = None
    return second




class Queue:
    def __init__(self):
        
        self.length = 0
        self.head = None
    def isEmpty(self):
        return (self.length == 0)
    def insert(self, cargo):
        node = Node(cargo)
        node.next = None
        if self.head == None:
                    
# if list is empty the new node goes first
            self.head = node
        else:
# find the last node in the list
            last = self.head
            while last.next: last = last.next
# append the new node
        last.next = node
        self.length = self.length + 1
    def remove(self):
        cargo = self.head.cargo
        self.head = self.head.next
        self.length = self.length - 1
        return cargo



    
