class Compnum:
    def __init__(self) -> None:
        pass
        
    def ShowNum(self,formula):
        print("The formula is:",formula)    
c=Compnum()
c.ShowNum("a+ib")

//parametrised

class Compnum:
    def __init__(self,r=0,i=0) -> None:
        self.real=r
        self.imag=i
        
    def ShowNum(self):
        print(self.real+(self.imag))    
c=Compnum(2,4)
c.ShowNum()
