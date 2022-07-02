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

//bankAccount

class Bank:
    def __init__(self,name,branch) -> None:
        self.Name=name
        self.Branch=branch
    def setName(self,name):
        self.Name=name
    def getName(self):
        return self.Name
b=Bank("Anju","Kozhikode")
print(b.getName())
b.setName("Zadu")
print(b.getName())
