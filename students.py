class Students:
    
    firstName =""
    lastName =" "
    age = 0
    
    def __init__(self,firstName, lastName,age):
        
        self.firstName = firstName
        self.lastName = lastName
        self.age = age
        
    def getFullName(self):
        return self.firstName+ "."+ self.lastName.upper()
    
    def isAgeSuperiorOrEqual(self, age):
        return self.age >=age
    
    def isLastnameStartsWith(self, startNameString):
        return self.lastName.startswith(startNameString.upper()) 