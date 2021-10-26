from university import University
from students import Students
from departement import Departement

my_Students1 = Students("Anoujean","Balachandran",23)
my_Students2 = Students("Nicolas","Soumare",18)
my_Students3 = Students("Pierre","Rabin",22)
my_Students4 = Students("CartMan","Boris",26)
my_Students5 = Students("Reput","Charlatan",27)
my_Students6 = Students("Raminette","Gardoum",14)
my_Students7 = Students("Juliette","Beherde",29)
my_Students8 = Students("Lamorti","Faxolp",16)



listStudents =[]

listStudents.append(my_Students1)
listStudents.append(my_Students2)

listStudents.append(my_Students3)
listStudents.append(my_Students4)

listStudents.append(my_Students5)
listStudents.append(my_Students6)

listStudents.append(my_Students7)
listStudents.append(my_Students8)


listDepartement = []
listDepartement.append(Departement("physique",listStudents))
listDepartement.append(Departement("informatique",listStudents))

university = University("CFA-INSTA",listDepartement)

print(university.getStudentsByArguments(22, "b"))

