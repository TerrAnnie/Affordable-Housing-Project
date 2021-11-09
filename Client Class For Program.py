#Class for a possible client using the software
#Code by TerrAnnie Scott


class Client():#Person class asks persons name, address, age and maritial status.Maybe rename to client 
    def __init__(self,firstname= "N/A", lastname= "N/A", age=0, city = "N/A", state ="N/A", Zip= 00000, StreetAddress = "N/A", Ismarried = False):
        self.firstname = firstname
        self.age= age
        self.lastname= lastname
        self.city = city
        self.state = state
        self.Zip= Zip
        self.StreetAddress = StreetAddress
        self.Ismarried = False
    def getname (self):
        firstname = self.firstname
        lastname= self.lastname
        name = firstname + " " + lastname
        return name
    def getage(self):
        return self.age
    def getAddress(self):
        Address = self.StreetAddress + " " +  self.city + " " + self.state + " " + self.Zip
        return Address
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



