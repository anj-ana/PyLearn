


class Rectangle:
    def __init__(self,length,width) -> None:
        self.len=length
        self.wid=width
    def Perimeter(self):
        return 2*((self.len)+(self.wid))
    def Area(self):
        return (self.len)*(self.wid)
    def Display(self):
        print("rectlen:",self.len)
        print("rectwid:",self.wid)
        print("rectperi:",self.Perimeter())
        print("rectarea:",self.Area())
r=Rectangle(3,5)
r.Display()
        
