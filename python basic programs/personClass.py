class person:
    def __init__(self,name, country,yob):
        self.name = name
        self.country = country
        self.yob = yob

    def findAge(self):
        return 2025 - self.yob
    
p1 = person("akshita","India",2004)
print(p1.findAge())
