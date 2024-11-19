# Encapsulation-Data Hiding
class BankAccount:
    def __init__(self, owner, balance=0):
        #self.owner = owner
        self.__balance = balance
        
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        
    def get_balance(self):
        return self.__balance

account = BankAccount("Alice", 100)
account.deposit(50)
print(account.get_balance()) # Outputs: 150