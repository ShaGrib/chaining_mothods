class User:
    bank_name = "First National Dojo"
    def __init__(self, name, email, balance):
        self.name = name
        self.email = email
        self.balance = balance
    def make_deposit(self, amount):
        self.balance += amount
        return self
    def make_withdraw(self, amount):
        self.balance -= amount
        return self
    def display_user_balance(self):
        print(f"{self.name}, Balance: ${self.balance}")


guido = User("Guido der Rothchild", "guido@python.com",100)
monty = User("Monty Python", "monty@python.com", 10100)
armen = User("Armen van Tollen", "armen@moomoomail.com", 450)
guido.bank_name = "Dojo Credit Union"

guido.display_user_balance()
monty.display_user_balance()
armen.display_user_balance()

guido.make_deposit(950).make_deposit(674).make_deposit(783).make_withdraw(1500).display_user_balance()
monty.make_deposit(1000).make_deposit(2500).make_withdraw(3000).make_withdraw(3500).display_user_balance()
armen.make_deposit(100).make_withdraw(87).make_withdraw(64).make_withdraw(450).display_user_balance()