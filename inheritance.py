class Person:
    def __init__(self,name,age) -> None:
        self.Name=name
        self.Age=age
    def ShowName(self):
        print(self.Name)
    def ShowAge(self):
        print(self.Age)
class Student:
    def __init__(self,rollno) -> None:
        self.Rollno=rollno
    def getRollno(self):
        print(self.Rollno)
class Resident(Person,Student):
    def __init__(self, name, age,rollno) -> None:
        Person.__init__(self,name,age)
        Student.__init__(self,rollno)
res=Resident("Anju",21,4)
res.ShowName()
res.ShowAge()
res.getRollno()
