from students import Students
class Departement:
    
    listEleve= []
    name = ""
    
    def __init__(self,name, allStudents):
        self.listEleve = allStudents
        self.name = name
        
       
    def getStudents(self):
        return self.listEleve
        
        