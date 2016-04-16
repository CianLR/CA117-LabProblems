class BankAccount:
    def __init__(self, balance=0):
        self.bal = float(balance)

    def deposit(self, ammount):
        self.bal += ammount

    def withdraw(self, ammount):
        if ammount > self.bal:
            print("Insufficient funds available")
        else:
            self.bal -= ammount

    def __str__(self):
        return 'Your current balance is: {:.2f} euro'.format(self.bal)
