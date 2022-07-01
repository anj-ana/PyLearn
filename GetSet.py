class Person:
    def __init__(self,Fname,Lname) -> None:
        self.name1=Fname
        self.name2=Lname
    def setName(self,Fname):
        self.name1=Fname
    def getName(self):
        return self.name1
p=Person("Anju","Sree")
print("NAME1:",p.getName())
p.setName("Anu")
print("Name2:",p.getName())