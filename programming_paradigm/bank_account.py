class BankAccount:
    def __init__(self,initial_balance):
        self.actual_balance = initial_balance
    def deposit(self,amount):
        if amount>0:
            self.account_balance += amount
            return True
        return False
    def withdraw(self,amount):
        
        if 0< amount<=self.account_balance:
            self.account_balance -= amount
            return True
        return False

    def display_balance(self):
        print(f"{self.actual_balance}")

    