# Assignment: BankAccount
# Objectives: Practice writing classes
#   Write a new BankAccount class:
#     The BankAccount class should have a balance. When a new BankAccount instance is created, if an amount is given, the balance of the account should initially be set to that amount; otherwise, the balance should start at $0. The account should also have an interest rate, saved as a decimal (i.e. 1% would be saved as 0.01), which should be provided upon instantiation. (Hint: when using default values in parameters, the order of parameters matters!)
# The class should also have the following methods:
#    deposit(self, amount) - increases the account balance by the given amount
#    withdraw(self, amount) - decreases the account balance by the given amount if there are sufficient funds; if there is not enough money, print a message "Insufficient funds: Charging a $5 fee" and deduct $5
#    display_account_info(self) - print to the console: eg. "Balance: $100"
#    yield_interest(self) - increases the account balance by the current balance * the interest rate (as long as the balance is positive)

# 1) Create a BankAccount class with the attributes interest rate and balance
# 2) Add a deposit method to the BankAccount class
# 3) Add a withdraw method to the BankAccount class
# 4) Add a display_account_info method to the BankAccount class
# 5) Add a yield_interest method to the BankAccount class
# 6) Create 2 accounts
# 7) To the first account, make 3 deposits and 1 withdrawal, then calculate interest and display the account's info all in one line of code (i.e. chaining)
# 8) To the second account, make 2 deposits and 4 withdrawals, then calculate interest and display the account's info all in one line of code (i.e. chaining)


class BankAccount:
    def __init__(self, int_rate=.01, balance=0):
        self.int_rate = int_rate
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        return self

    def withdraw(self, amount):
        self.balance -= amount
        if(self.balance < 0):
            print("Insufficient funds: Charging a $5 fee")
            self.balance -= 5
        return self

    def display_account_info(self):
        print(f"Account Balance: {self.balance}, Yield: {self.yield_rate}")

    def yield_interest(self):
        self.yield_rate = (self.balance * self.int_rate)
        if(self.balance > 0):
            self.balance += self.yield_rate
        return self


account_1 = BankAccount()
account_2 = BankAccount()

account_1.deposit(100).deposit(200).deposit(300).withdraw(50).yield_interest().display_account_info()

account_2.deposit(100).deposit(200).withdraw(10).withdraw(10).withdraw(10).withdraw(20).yield_interest().display_account_info()
