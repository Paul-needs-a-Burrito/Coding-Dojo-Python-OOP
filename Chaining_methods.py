# Assignment: Chaining methods
#     Objectives:
#         Understand how to chain methods

# 1) Update your previous assignment so that each instance's methods are chained


class User:
    def __init__(self, username):
        self.name = username
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount
        return self

    def make_withdrawl(self, amount):
        self.account_balance -= amount
        return self

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount
        return self


alan = User("Alan")
bob = User("Bob")
chris = User("Chris")

alan.make_deposit(100).make_deposit(50).make_deposit(25).make_withdrawl(10).display_user_balance()

bob.make_deposit(200).make_deposit(200).make_withdrawl(50).make_withdrawl(50).display_user_balance()

chris.make_deposit(300).make_withdrawl(50).make_withdrawl(50).make_withdrawl(50).display_user_balance()

alan.transfer_money(chris, 5).display_user_balance()
chris.display_user_balance()
