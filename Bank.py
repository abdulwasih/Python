class Bank:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.status="No account"
        self.balance=0
    def openaccount(self,initialbalnce):
        self.balance=self.balance+initialbalnce
        print("Your account with name "+self.name+" has been opened with "+str(self.balance)+" as initial balance")
        self.status="Opened"
    def deposit(self,depbalance):
        if self.status=="Opened":
            self.balance=self.balance+depbalance
            print("Your current balance is",self.balance)
        else:
            print("Sorry,You've no account yet..!,Please create a new one")
    def withdraw(self,withbalance):
        if self.status=="Opened" and self.balance>=withbalance:
            self.balance=self.balance-withbalance
            print("Your current balance is",self.balance)
        else:
            print("Sorry..!,You've no account or you've no sufficient balance")



