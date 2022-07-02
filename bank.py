class BankAccount:
    def __init__(self,acc_no,name,balance) -> None:
        self.Account=acc_no
        self.Name=name
        self.Bal=balance

    def Deposit(self,deposit):
        self.Bal=self.Bal+ deposit
    def Withdraw(self,withdraw):
        self.Bal=self.Bal-withdraw
    def Bankfee(self):
        self.Bal=(45/100)*self.Bal
    def Display(self):
        print(self.Account)
        print(self.Name)
        print(self.Bal)
bank=BankAccount(112233,"Anju",50000)
bank.Display()

