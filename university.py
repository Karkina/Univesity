from departement import Departement
from functools import reduce

class University :
    name=''
    listDepartement= []

    def __init__(self, name, departement):
        
        self.name = name
        self.listDepartement = departement
        
    def getFirstDepart(self):
        return self.listDepartement[0]
        
    def getStudentsByAge22(self):
        return self.getStudentsByLambda(lambda student: student.isAgeSuperiorOrEqual(22));    
    
    def getStudentsByArguments(self, age,startNameString):
        return self.getStudentsByLambda(lambda student: student.isAgeSuperiorOrEqual(age) 
                                        and student.isLastnameStartsWith(startNameString));
  
    def getStudentsByLambda(self, lambdaFun):
         return list(map(lambda s: s.getFullName(),
                        list(filter( lambdaFun,
                                    self.getConcatenateListDepartment()))))
     
    def getConcatenateListDepartment(self):
        return list(set(reduce(lambda x,y:x.getStudents()+y.getStudents(),self.listDepartement)))
    
    