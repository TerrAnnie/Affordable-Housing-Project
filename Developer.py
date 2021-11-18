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


class Developer():
    def __init__(self,InvestmentRange = 0,DevelopmentType= False,  LandSize= "N/A", ZonedFor = "N/A"):#False == mixed income, true == low income
       self.InvestmentRange = InvestmentRange
       self.DevelopmentType = DevelopmentType
       self.LandSize = LandSize
       self.ZonedFor = ZonedFor
       self.Category = "N/A"
       self.Develop = "N/A"
       self.LotType = "N/A"
       self.DevelopStr = "N/A"
    def getInvestment(self):
        return self.InvestmentRange
    def getDevelopmentType(self):
        return self.DevelopmentType
    def getCategory(self):
        return self.Category
    def BuildType(self, TypeofBuild):
        if TypeofBuild == 1:
                return "Scattered Site Development"
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
        elif LandSize == "CONTIGUOUS" or LandSize =="ONE LARGE LOT":
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
        self.InvestmentRangeFacts()
       
        self.SetLotType()##Set the lot type
        if self.IsZonable() == True:
            if self.DevelopmentType == True:

                if self.Category == "LOW" and self.LotType == "Multiple/one small":
                    
                    if self.ZonedFor == "R-10" or self.ZonedFor == "R-5" or self.ZonedFor == "R-2.5":
                        self.Develop =  self.BuildType(1)
                elif self.Category == "MEDIUM" and self.LotType == "Contiguous":
                      
                        if self.ZonedFor == "R-0.5" or self.ZonedFor == "R-1.5" or self.ZonedFor == "R-2.5" or self.ZonedFor == "R-0.3":
                            self.Develop = self.BuildType (4)
                elif self.Category == "HIGH" and self.LotType == "Contiguous":
                        if self.ZonedFor == "R-0.5" or self.ZonedFor == "R-1.5" or self.ZonedFor == "R-0.3":
                            self.Develop = BuildType (2)
            else:
                    if self.Category == "LOW" and self.LotType == "Multiple/one small":
                        if self.ZonedFor == "R-10" or self.ZonedFor == "R-5" or self.ZonedFor == "R-2.5":
                            self.Develop =  self.BuildType(1)
                    elif self.Category == "MEDIUM" and self.LotType == "Contiguous":
                        if self.ZonedFor == "R-0.5" or self.ZonedFor == "R-1.5" or self.ZonedFor == "R-0.3":
                            self.Develop = self.BuildType (2)
                    elif self.Category == "HIGH" and self.LotType == "Contiguous":
                        if self.ZonedFor == "R-0.5" or self.ZonedFor == "R-1.5" or self.ZonedFor == "R-0.3":
                            self.Develop = BuildType (3)
            
        
    def PrintToFile(self):#Add remaning text Zoned For and Lot Type
        self.DevelopmentFacts()
        file_open= open("Property Facts.txt","w")
        file_open.write(("Your investment is $%d." % (self.getInvestment())))
        file_open.write("\n \n")
        if self.DevelopmentType == True:#If its low income
        
            
            file_open.write("Because your development is intended to be low-income,categorized as %s, is zoned for %s, and the lot type is %s we reccomend this type of building: %s" % (self.Category,self.ZonedFor, self.LotType,self.Develop))

        else:
            file_open.write("Because your development is intended to be low-income,categorized as %s, is zoned for %s, and the lot type is %s we reccomend this type of building: %s" % (self.Category, self.Develop,self.ZonedFor, self.LotType))


        file_open.close()
            
                    
                    
                




