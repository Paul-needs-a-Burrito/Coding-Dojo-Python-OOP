# Assignment: Users with Bank Accounts
# Objectives:
#     Practice writing classes with associations
# Update your existing User class to have an association with the BankAccount class. Make sure that by the end of this assignment that you:
# have both the User and BankAccount classes in the same file for your assignment,
# only create BankAccount instances inside of the User's __init__ method, and
# only call BankAccount methods inside of the methods in the User class
# 1) Update the User class __init__ method
# 2) Update the User class make_deposit method
# 3) Update the User class make_withdrawal method
# 4) Update the User class display_user_balance method
# 5) SENSEI BONUS: Allow a user to have multiple accounts; update methods so the user has to specify which account they are withdrawing or depositing to


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


class User:
    def __init__(self, username):
        self.name = username
        self.account = [BankAccount(), BankAccount()]

    def make_deposit(self, amount, account_number=0):
        self.account[account_number].balance += amount
        return self

    def make_withdrawl(self, amount, account_number=0):
        self.account[account_number].balance -= amount
        return self

    def display_user_balance(self, account_number=0):
        print(f"User: {self.name}, Account #:{account_number}, Balance: ${self.account[account_number].balance}")
        return self

    def transfer_money(self, other_user, amount, from_account=0, to_account=0):
        self.account[from_account].balance -= amount
        other_user.account[to_account].balance += amount
        return self


alan = User("Alan")
bob = User("Bob")
chris = User("Chris")

alan.make_deposit(100, 0).make_deposit(50, 1).make_deposit(25, 1).make_withdrawl(10, 0).display_user_balance(0).display_user_balance(1)

bob.make_deposit(200, 0).make_deposit(200, 1).make_withdrawl(50, 0).make_withdrawl(50, 0).display_user_balance(0).display_user_balance(1)

chris.make_deposit(300).make_withdrawl(50).make_withdrawl(50).make_withdrawl(50).display_user_balance()

alan.transfer_money(chris, 5, 1).display_user_balance(1)
chris.display_user_balance()
