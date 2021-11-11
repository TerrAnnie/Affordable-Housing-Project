#Developer Class

#what kind of development?(low income ) Low income true.
#GetInvestment

#Target Property
#Option for senior living
#Cateogory 

class Developer():
    def __init__(self,InvestmentRange = 0,DevelopmentType= False):#False == mixed income, true == low income
       self.InvestmentRange = InvestmentRange
       self.DevelopmentType = DevelopmentType
       self.Category = "N/A"
       self.Develop = "N/A"
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
    def InvestmentRangeFacts(self):
        IR = self.InvestmentRange
        if IR <= 3000000:
            self.Category = "LOW"
        elif IR >= 3000000 and IR <= 5000000:
            self.Category = "MEDIUM"
        else:
            self.Category = "HIGH"
    def DevelopmentFacts(self):
        
        if self.DevelopmentType == True:
            if self.Category == "LOW":
                self.Develop =  self.BuildType(1)
            elif self.Category == "MEDIUM":
                self.Develop = self.BuildType (4)
            else:
                self.Develop = BuildType (2)
        else:
            if self.Category  == "LOW":
                self.Develop =  self.BuildType(1)
            elif self.Category == "MEDIUM":
                self.Develop = self.BuildType (2)
            else:
                self.Develop = self.BuildType (3)

        
       
        
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



