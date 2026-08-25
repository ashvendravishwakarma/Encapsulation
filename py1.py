class BankAccount:
    def __init__(self,account_holder):
        self.name=account_holder
        self.__balance=0

    def deposit(self,balance):
        if balance>0:
            self.__balance+=balance
        else:
            print("pleace inter sufficient amount")

    def withdraw(self,balance):
        if balance<=self.__balance:
            self.__balance-=balance
        else:
            print("not money in your account")

    def get_balance(self):
        return self.__balance
#my name is ashvendra vishwakarm 
BA1=BankAccount("rohan")
BA1.deposit(50000)
BA1.withdraw(400)
print(BA1.name, BA1.get_balance())
