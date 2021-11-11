#Class for a possible client using the software
#Code by TerrAnnie Scott


#Class for a possible client using the software
#Code by TerrAnnie Scott
#closefile in developer
#Implement printing basic info to file

class Client():#Person class asks persons name, address, age and maritial status.Maybe rename to client 
    def __init__(self,firstname= "N/A", lastname= "N/A", age=0, city = "N/A", state ="N/A", Zip= 00000, StreetAddress = "N/A", Target_Zip=00000):
        self.firstname = firstname
        self.age = age
        self.lastname= lastname
        self.city = city
        self.state = state
        self.Zip= Zip
        self.StreetAddress = StreetAddress
        self.Target_Zip = Target_Zip
        self.PrintList =[]
        self.InOppurtunityZone = False
      
    def getname (self):
        firstname = self.firstname
        lastname= self.lastname
        name = firstname + " " + lastname
        return name
    def getage(self):
        return self.age
    def getAddress(self):
        Zipcode = str(self.Zip)
        Address = self.StreetAddress + " " +  self.city + " " + self.state + " " + Zipcode
        return Address
    def GetMarried(self):
        return self.Ismarried
  
        
    
    def OppurtunityZoneCheck(self):
      
        string = "N/A"
        ZipCode = "N/A"
        with open("Oppurtunity Zone Zipcodes.txt", "r") as open_zipcodes:
            for line in open_zipcodes:
                if '*' in line:
                    Zipcode = int(line[0:5])#slice the line check. to only obtain zipcode
                    self.PrintList.append("This Zipcode may be in an oppurtunity zone. You may be eligible to receive preferential tax treatment from the IRS.")
                else:
                    Zipcode = int(line)
                    self.PrintList.append("This Zipcode is in an oppurtunity zone. You may be eligible to receive preferential tax treatment from the IRS.")

                if Zipcode == self.Target_Zip:
                    self.InOppurtunityZone = True
                    break
        open_zipcodes.close()
      
            
    def PrintAllInfo (self):
        self.OppurtunityZoneCheck()
        file_open = open("Client Property Facts.txt", "w")
        file_open.write("Here's all the information we have on file:")
        file_open.write ("\n")
        file_open.write ("Name:  %s" % (self.getname()))
        file_open.write ("\n")
        file_open.write ("Age:  %s" % (self.age))
        file_open.write ("\n")
        file_open.write ("Address:  %s" % (self.getAddress()))
        file_open.write ("\n")
        file_open.write ("Target Property Zipcode:  %d" % (self.Target_Zip))
        file_open.write ("\n")
        if self.InOppurtunityZone == True:
             file_open.write(self.PrintList[1])#Do make a loop here later
        file_open.close()

        
C1 = Client("TerrAnnie","Scott","21","KC","MO",64138, "blah", 64116)
C1.PrintAllInfo()




