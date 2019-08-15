class Dog:

    def __init__(self,name):
        self.name = name
        self.tricks = []

    def add_trick(self,trick):
        self.tricks.append(trick)
    def __str__(self):
        return self.name
    
class Dog2:
    tricks = []
    def __init__(self,name):
        self.name = name
    def add_trick(self,trick):
        self.tricks.append(trick)
