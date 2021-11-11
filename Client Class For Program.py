#Class for a possible client using the software
#Code by TerrAnnie Scott


#Class for a possible client using the software
#Code by TerrAnnie Scott
#closefile in developer

class Client():#Person class asks persons name, address, age and maritial status.Maybe rename to client 
    def __init__(self,firstname= "N/A", lastname= "N/A", age=0, city = "N/A", state ="N/A", Zip= 00000, StreetAddress = "N/A", Target_Zip=00000):
        self.firstname = firstname
        self.age= age
        self.lastname= lastname
        self.city = city
        self.state = state
        self.Zip= Zip
        self.StreetAddress = StreetAddress
        self.Target_Zip = Target_Zip
      
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
    def OppurtunityZoneCheck(self):
        InOppurtunityZone = False
        string = "N/A"
        ZipCode = "N/A"
        with open("Oppurtunity Zone Zipcodes.txt", "r") as open_zipcodes:
            for line in open_zipcodes:
                if '*' in line:
                    Zipcode = int(line[0:5])
                    string= "This Zipcode may be in an oppurtunity Zone"
                else:
                    Zipcode = int(line)
                    string = "This Zipcode is an oppurtunity zone"

                if Zipcode == self.Target_Zip:
                    InOppurtunityZone = True
                    break
        open_zipcodes.close()
        if InOppurtunityZone == True:
            print(string)

C1 = Client("TerrAnnie","Scott","21","KC","MO",64138, "blah", 64116)
C1.OppurtunityZoneCheck()
            



