#Class for a possible client using the software
#Code by TerrAnnie Scott


class Client():#Person class asks persons name, address, age and maritial status.Maybe rename to client 
    def __init__(self,firstname= "N/A", lastname= "N/A", age=0, city = "N/A", state ="N/A", Zip= 00000, StreetAddress = "N/A"):
        self.firstname = firstname
        self.age= age
        self.lastname= lastname
        self.city = city
        self.state = state
        self.Zip= Zip
        self.StreetAddress = StreetAddress
        self.Ismarried= False
    def getname (self):
        firstname = self.firstname
        lastname= self.lastname
        name = firstname + " " + lastname
        return name
    def setname (self):
        self.firstname = input("What is your first name?  ")
        self.lastname = input("What is your last name?   ")
    def setage(self):
        self.age =  int (input("What is your current age? "))
    def getage(self):
        return self.age
    def setAddress(self):
        self.StreetAddress = input("Enter Your Street Address (Excluding Zip, City, and State) ")
        self.city= input("Enter Your City")
        self.state = input("Enter Your State ")
        self.Zip= input("Enter Your ZipCode ")
    def getAddress(self):
        Address = self.StreetAddress + " " +  self.city + " " + self.state + " " + self.Zip
        return Address
    def Setmarried(self):
        MaritalStatus= input("Are you Married? Y for yes N for no")
        MaritalStatus.upper()
        if(MaritalStatus == "Y"):
            self.Ismarried = True
    def GetMarried(self):
        return self.Ismarried
    def PrintAllInfo (self):
        print("Here is the information we have on file.")
        print()
        print(self.getname())
        print(self.getage())
        print(self.getAddress())
        if(self.GetMarried()):
            print("Marriage Status = Yes")
        else:
            print("Marriage Status = NO")
        
    
    

C1 = Client()
C1.setname()
C1.setage()
C1.setAddress()
C1.Setmarried()
C1.PrintAllInfo()



