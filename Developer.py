#Developer Class

#what kind of development?(low income ) Low income true.
#GetInvestment

#Target Property
#Option for senior living
#Cateogory 
#Is the land one small lot (1 acre or less), one large lot (more than 1 acre), contiguous lots, multiple lots, or unknown?


class Developer():
    def __init__(self,InvestmentRange = 0,DevelopmentType= False,  LandSize= "N/A", ZonedFor = "N/A"):#False == mixed income, true == low income
       self.InvestmentRange = InvestmentRange
       self.DevelopmentType = DevelopmentType
       self.LandSize = LandSize
       self.ZonedFor = ZonedFor
       self.Category = "N/A"
       self.Develop = "N/A"
       self.LotType = "N/A"
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
    def LotType(self):
        LandSize = self.LandSize.upper()#Take care of casing
        if self.LandSize == "ONE SMALL LOT" or self.LandSize =="MULTIPLE LOTS":
            self.LotType = "Multiple/one small"
        elif self.LandSize == "CONTIGUOUS" or self.LandSize =="ONE LARGE LOT":
            self.LotType = "Contiguous"
        else:
            self.LotType = "Inquire with the KC Land Bank to find developable land. https://www.kcmolandbank.org/"
            
    def IsZonable(self):
        if self.ZonedFor == "R-80":
            return False
            
            
        
    def InvestmentRangeFacts(self):
        IR = self.InvestmentRange
        if IR <= 3000000:
            self.Category = "LOW"
        elif IR >= 3000000 and IR <= 5000000:
            self.Category = "MEDIUM"
        else:
            self.Category = "HIGH"
    def DevelopmentFacts(self):
        
        if self.IsZonable == True:
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
                if self.DevelopmentType == True:
                    if self.Category == "LOW" and self.LotType == "Multiple/one small":
                        if self.ZonedFor == "R-10" or self.ZonedFor == "R-5" or self.ZonedFor == "R-2.5":
                            self.Develop =  self.BuildType(1)
                    elif self.Category == "MEDIUM" and self.LotType == "Contiguous":
                        if self.ZonedFor == "R-0.5" or self.ZonedFor == "R-1.5" or self.ZonedFor == "R-0.3":
                            self.Develop = self.BuildType (2)
                    elif self.Category == "HIGH" and self.LotType == "Contiguous":
                        if self.ZonedFor == "R-0.5" or self.ZonedFor == "R-1.5" or self.ZonedFor == "R-0.3":
                            self.Develop = BuildType (3)
            
       
        
    def PrintToFile(self):
        self.InvestmentRangeFacts()
        self.DevelopmentFacts()
        file_open= open("Property Facts.txt","w")
        file_open.write(("Your investment is $%d." % (self.getInvestment())))
        file_open.write("\n \n")
        if self.DevelopmentType == True:
            file_open.write(("Because your development is intended to be low-income and categorized as %s we reccomend this type of building: %s" % (self.Category, self.Develop)))
        else:
            file_open.write(("Because your development is intended to be mixed-income and categorized as %s we reccomend this type of building: %s" % (self.Category, self.Develop)))

        file_open.close()
            
                    
                    
                
D1= Developer(4000000, True)
D1.PrintToFile()



