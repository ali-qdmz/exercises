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
