# Here is a BankAccount class containing custom methods
class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance

    # Here is a method to deposit money into the account
    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ${amount}. New balance: ${self.balance}")

    # Here is a method to withdraw money with a balance check
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew ${amount}. Remaining balance: ${self.balance}")
        else:
            print("Insufficient funds for this withdrawal.")

# Here is creating an account object and calling its methods
my_account = BankAccount("Amina", 100)
my_account.deposit(50)
my_account.withdraw(70)
my_account.withdraw(100)