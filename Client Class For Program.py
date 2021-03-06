#Class for a possible client using the software
#Code by TerrAnnie Scott


#Class for a possible client using the software
#Code by TerrAnnie Scott
#closefile in developer
#Implement printing basic info to file
#Is Homeowner
#IsDisabled
#If Mortgage

class Client():#Person class asks persons name, address, age and maritial status.Maybe rename to client 
    def __init__(self, name= "N/A", age=0, StreetAddress = "N/A", Zip = 00000, Target_Zip = 00000):
        self.name = name
        self.age = age
        self.Zip= Zip
        self.StreetAddress = StreetAddress
        self.Target_Zip = Target_Zip
        self.PrintList =[]
        self.InOppurtunityZone = False
        self.IsMarried = False
        self.IsDisabled = False
        self.HasMortgage = False
        self.IsHomeowner = False
        self.PaidTaxes = False
        self.CircuitBreaker = False
        self.InterestDeduction = False
        self.PropertyTaxDeduction = False
        self.CircuitbreakerStr= ""
        self.HomeownerMortgageStr= "N/A"
        self.HomeownerTaxesStr= "N/A"
        self.OppurtunityZoneStr= "N/A"
        self.TaxIfThenCheck = False
        
    def setBooleans(self,IsMarried = False,IsDisabled = False, HasMortgage= False, IsHomeowner=False, PaidTaxes= False):
        self.IsMarried = IsMarried #true if married
        self.IsDisabled = IsDisabled #True if Disabled
        self.HasMortgage = HasMortgage# True if have mortgage
        self.IsHomeowner = IsHomeowner# True if they are homeowner false if they are a renter
        self.PaidTaxes = PaidTaxes #True if they paid taxes

    def test(self):#for tests
        if self.IsDisabled == True:
            print ("Works")
      
    def getname (self):
        return self.name
    def getage(self):
        return self.age
    def getAddress(self):
        Zipcode = str(self.Zip)
        Address = self.StreetAddress + " " + Zipcode
       
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
                    
                if '*' not in line:
                    Zipcode = int(line)

                if Zipcode == self.Target_Zip:
                    self.InOppurtunityZone = True
                    string = "This Zipcode may be in an oppurtunity zone. You may be eligible to receive preferential tax treatment from the IRS."
                    self.OppurtunityZoneStr= string
                    self.PrintList.append("This target Zipcode may be in an oppurtunity zone. You may be eligible to receive preferential tax treatment from the IRS.")
                    break
        open_zipcodes.close()


    def getOppurtunityZone(self):
        self.OppurtunityZoneCheck()
        if self.InOppurtunityZone == True:
             return self.OppurtunityZoneStr



    def SetTaxIfThen(self):
        string = "N/A"
        self.TaxIfThenCheck = True
        if self.age >= 65 or self.IsDisabled == True:
            self.CircuitBreaker = True
            if self.IsHomeowner == True and self.IsDisabled == True:
                string ="Because you are a homeowner with a disability, you are eligible for Missouri Property Tax Credit Claim (circuit breaker) up to $1,100"     
            elif self.IsHomeowner == True and self.age >= 65:
               
                string = "Because you are a homeowner 65 years of age or older, you are eligible for Missouri Property Tax Credit Claim (circuit breaker) up to $1,100"
            elif self.IsHomeowner == False and self.age >= 65:
             
                string= "Because you are a renter 65 years of age or older, you are eligible for Missouri Property Tax Credit Claim (circuit breaker) up to $750"
            elif self.IsHomeowner == False and self.IsDisabled == True:
               
                string = "Because you are a renter with a disability, you are eligible for Missouri Property Tax Credit Claim (circuit breaker) up to $750"
            
            self.PrintList.append(string)
            self.CircuitbreakerStr = string
                  
        if self.IsHomeowner == True:
            if self.HasMortgage == True:
                self.InterestDeduction = True
                self.HomeownerMortgageStr = "Interests accrued on mortgage is deductible from taxable income (I.R.C. ??163(h))"
                self.PrintList.append("Interests accrued on mortgage is deductible from taxable income (I.R.C. ??163(h))")
            if self.PaidTaxes == True:
                self.PropertyTaxDeduction = True
                string=("Because you paid taxes, money paid for property taxes are deductible from taxable income up to 10k (I.R.C. ??164)")
                self.PrintList.append(string)
                self.HomeownerTaxesStr= string
                
    def GetCircuitBreaker(self):#Gets circuit breaker string
        if self.TaxIfThenCheck ==False:
            self.SetTaxIfThen()
        if self.CircuitBreaker == True:
           return self.CircuitbreakerStr
    def GetHomeownerMortgage(self):#get HomeownerMortgage string
        if self.TaxIfThenCheck ==False:
            self.SetTaxIfThen()
        if self.InterestDeduction ==True:
            return self.HomeownerMortgageStr
    def GetPropDeduction(self):
        if self.TaxIfThenCheck ==False:
            self.SetTaxIfThen()
        if self.PropertyDeduction == True:
            return self.HomeownerTaxesStr
        
                


            
    def PrintAllInfo (self):
        self.OppurtunityZoneCheck()
        self.SetTaxIfThen()
        file_open = open("Client Property Facts.txt", "w")
        file_open.write("Here's all the information we have on file:")
        file_open.write ("\n")
        file_open.write ("Name:  %s" % (self.getname()))
        file_open.write ("\n")
        file_open.write ("Age:  %d" % (self.age))
        file_open.write ("\n")
        file_open.write ("Address:  %s" % (self.getAddress()))
        file_open.write ("\n")
        file_open.write ("Target Property Zipcode:  %d" % (self.Target_Zip))
        file_open.write ("\n")
        file_open.write ("\n")
        for data in self.PrintList:
            file_open.write("\n")
            file_open.write(data)
            file_open.write("\n")
        file_open.close()

        
C1 = Client("TerrAnnie Scott",21,"KC MO",64138, 64116)
C1.setBooleans(False,True, False, True, True)
C1.test()
C1.PrintAllInfo()
print(C1.GetHomeownerMortgage())


