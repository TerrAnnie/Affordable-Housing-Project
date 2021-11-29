#Developer Class

#what kind of development?(low income ) Low income true.
#GetInvestment

#Target Property
#Option for senior living
#Cateogory 
#Is the land one small lot (1 acre or less), one large lot (more than 1 acre), contiguous lots, multiple lots, or unknown?
#To Do: File writing, String formatting,Testing
#Check if file already exists if so we can collect already inputed information
#Create a file with Common Defenitions and Links
#Make Key Value pair
#Blighted area or Conservation area 

class Developer():
    def __init__(self,InvestmentRange = 0,DevelopmentType= False,  LandSize= "N/A", ZonedFor = "N/A", DevSiteType = "N/A"):#False == mixed income, true == low income
       self.InvestmentRange = InvestmentRange
       self.DevelopmentType = DevelopmentType
       self.LandSize = LandSize
       self.ZonedFor = ZonedFor
       self.Category = "N/A"
       self.Develop = "N/A"
       self.LotType = "N/A"
       self.DevelopStr = "N/A"
       self.DevSiteType = DevSiteType
       self.TaxIncrementStr = "N/A"
    def getInvestment(self):
        return self.InvestmentRange
    def getDevelopmentType(self):
        return self.DevelopmentType
    def getCategory(self):
        return self.Category
    def BuildType(self, TypeofBuild):
        if TypeofBuild == 1:
                return ("Scattered Site Development")

 
        if TypeofBuild == 2:
                return "Apartment Building"
        if TypeofBuild == 3:
                return "Condominium Building"
        if TypeofBuild == 4:
                return "Clustered Development"
    def SetLotType(self):
        LandSize = self.LandSize.upper()#Take care of casing
        if LandSize == "ONE SMALL LOT" or LandSize =="MULTIPLE LOTS":
            self.LotType = "Multiple/one small"
        elif LandSize == "CONTIGUOUS LOTS" or LandSize =="ONE LARGE LOT":
            self.LotType = "Contiguous"
        else:
            self.LotType = "Inquire with the KC Land Bank to find developable land. https://www.kcmolandbank.org/"
            
    def IsZonable(self):
        if self.ZonedFor == "R-80":
            self.Develop = "Parcel may not be developable. Check for variances in zoning of this area."
            return False
        else:
            return True
            
    def getDevelop(self):
        return self.Develop
        
        
    def InvestmentRangeFacts(self):
        IR = self.InvestmentRange
        if IR <= 3000000:
            self.Category = "LOW"
        elif IR >= 3000000 and IR <= 5000000:
            self.Category = "MEDIUM"
        else:
            self.Category = "HIGH"
    def DevelopmentFacts(self):
        Correct = False
  
        self.InvestmentRangeFacts()
       
       
        self.SetLotType()##Set the lot type
        if self.IsZonable() == True:
            if self.DevelopmentType == True:
                  
               

                if self.Category == "LOW" and self.LotType == "Multiple/one small":
                    if self.ZonedFor == "R-10" or self.ZonedFor == "R-5" or self.ZonedFor == "R-2.5":
                        self.Develop =  self.BuildType(1)
                        Correct = True
                elif self.Category == "MEDIUM" and self.LotType == "Contiguous":
                      if self.ZonedFor == "R-0.5" or self.ZonedFor == "R-1.5" or self.ZonedFor == "R-2.5" or self.ZonedFor == "R-0.3":
                            self.Develop = self.BuildType (4)
                            Correct = True
                elif self.Category == "HIGH" and self.LotType == "Contiguous":
                        if self.ZonedFor == "R-0.5" or self.ZonedFor == "R-1.5" or self.ZonedFor == "R-0.3":
                            self.Develop = BuildType (2)
                            Correct = True

            else:
                    if self.Category == "LOW" and self.LotType == "Multiple/one small":
                        if self.ZonedFor == "R-10" or self.ZonedFor == "R-5" or self.ZonedFor == "R-2.5":
                            self.Develop =  self.BuildType(1)
                            Correct = True
                    elif self.Category == "MEDIUM" and self.LotType == "Contiguous":
                        if self.ZonedFor == "R-0.5" or self.ZonedFor == "R-1.5" or self.ZonedFor == "R-0.3":
                            self.Develop = self.BuildType (2)
                            Correct = True
                    elif self.Category == "HIGH" and self.LotType == "Contiguous":
                        if self.ZonedFor == "R-0.5" or self.ZonedFor == "R-1.5" or self.ZonedFor == "R-0.3":
                            self.Develop = BuildType (3)
                            Correct = True
            if Correct == True and self.DevelopmentType == True:
                self.DevelopStr = "Because your development is intended to be low-income,categorized as %s, is zoned for %s, and the lot type is %s we reccomend this type of building: %s" % (self.Category,self.ZonedFor, self.LotType,self.Develop)
            elif Correct == True and self.DevelopmentType == False:
                self.DevelopStr = "Because your development is intended to be mixed-income,categorized as %s, is zoned for %s, and the lot type is %s we reccomend this type of building: %s" % (self.Category,self.ZonedFor, self.LotType,self.Develop)

                
            else:
               
                self.DevelopStr = "At the time, we can not give you our building reccomendations."
    def SetDevSite(self):
        if self.DevSiteType.upper() == "BLIGHTED AREA" or self.DevSiteType.upper() == "CONSERVATION AREA":
           
            self.TaxIncrementStr = "Because you Developemnt site is a Blighted Area or Conservation area, you are Eligble for Tax Increment Financing"
      
            
    def GetDevSite(self):
        self.SetDevSite()
        return self.TaxIncrementStr

    def GetDevelopmentFacts(self):
        self.DevelopmentFacts()
        
        if self.IsZonable == False:
            
            return self.Develop
        else:
            return self.DevelopStr

        
    def PrintToFile(self):#Add remaning text Zoned For and Lot Type
        self.DevelopmentFacts()
        self.SetDevSite()
        file_open= open("Property Facts.txt","w")
        file_open.write(("Your investment is $%d." % (self.getInvestment())))
        file_open.write("\n \n")
        if self.DevelopStr != "N/A":
            file_open.write(self.DevelopStr)
            file_open.write("\n")

        if self.TaxIncrementStr != "N/A":
            file_open.write(self.TaxIncrementStr)

        file_open.close()
            
                    
                    


D1 = Developer(1000,True, "One small lot", "R-10", "blighted area")
D1.PrintToFile()


