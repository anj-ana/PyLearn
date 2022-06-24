


class Employee:
    def __init__(self,name,id,dept):
        self.name=name
        self.id=id
        self.dept=dept
    def showDetails(self):
        print("Name:",self.name)  
        print("Id:",self.id) 
        print("Dept:",self.dept) 
e=Employee("anju",123,"cse")
e.showDetails()
        

     

