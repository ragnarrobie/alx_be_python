class BankAccount:
    def __init__(self,initial_balance):
        self.actual_balance = initial_balance
    def display_balance(self):
        print(f"{self.actual_balance}")

    def deposit(self,amount):
        account_balance += amount
    def withdraw(self,amount):
        boo = self.account_balance - amount
        if boo<0:
            return False, amount
        else:
            return True,boo
    