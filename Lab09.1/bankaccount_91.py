class BankAccount:
    next_account_number = 16555232

    def __init__(self, forename, surname, balance):
        self.forename = forename
        self.surname = surname
        self.balance = balance
        self.account_number = self.next_account_number

        self.__class__.next_account_number += 1

    def lodge(self, amount):
        self.balance += amount

    def __str__(self):
        ret_str = 'Name: {} {}'.format(self.forename, self.surname)
        ret_str += '\nAccount number: {}'.format(self.account_number)
        ret_str += '\nBalance: {:.2f}'.format(self.balance)
        return ret_str


class CurrentAccount(BankAccount):
    account_type = 'current'
    overdraft = 1000.00

    def withdraw(self, amount):
        if self.balance + self.overdraft >= amount:
            self.balance -= amount
        else:
            print("Insufficent funds available")

    def __str__(self):
        ret_str = super().__str__()
        ret_str += '\nAccount type: {}'.format(self.account_type)
        return ret_str


class SavingsAccount(BankAccount):
    account_type = 'savings'
    interest_rate = 0.01

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("Insufficent funds available")

    def apply_intrest(self):
        self.balance *= 1 + self.interest_rate

    def __str__(self):
        ret_str = super().__str__()
        ret_str += '\nAccount type: {}'.format(self.account_type)
        return ret_str
