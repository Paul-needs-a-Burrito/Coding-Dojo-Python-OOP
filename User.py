# Assignment: User
#   Objectives:
#    Practice creating a class and making instances from it
#    Practice accessing the methods and attributes of different instances
# 1) Create a file with the User class, including the __init__ and make_deposit methods
# 2) Add a make_withdrawal method to the User class
# 3) Add a display_user_balance method to the User class
# 4) Create 3 instances of the User class
# 5) Have the first user make 3 deposits and 1 withdrawal and then display their balance
# 6) Have the second user make 2 deposits and 2 withdrawals and then display their balance
# 7) Have the third user make 1 deposits and 3 withdrawals and then display their balance
# BONUS: Add a transfer_money method; have the first user transfer money to the third user and then print both users' balances


class User:
    def __init__(self, username):
        self.name = username
        self.account_balance = 0

    def make_deposit(self, amount):
        self.account_balance += amount

    def make_withdrawl(self, amount):
        self.account_balance -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: ${self.account_balance}")

    def transfer_money(self, other_user, amount):
        self.account_balance -= amount
        other_user.account_balance += amount


alan = User("Alan")
bob = User("Bob")
chris = User("Chris")

alan.make_deposit(100)
alan.make_deposit(50)
alan.make_deposit(25)
alan.make_withdrawl(10)
alan.display_user_balance()

bob.make_deposit(200)
bob.make_deposit(200)
bob.make_withdrawl(50)
bob.make_withdrawl(50)
bob.display_user_balance()

chris.make_deposit(300)
chris.make_withdrawl(50)
chris.make_withdrawl(50)
chris.make_withdrawl(50)
chris.display_user_balance()

alan.transfer_money(chris, 5)
alan.display_user_balance()
chris.display_user_balance()
