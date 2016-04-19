class BankAccount:
    next_account_number = 18555666

    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
        self.transactions = ['Opening balance: {:.2f}'.format(balance)]
        self.account_number = self.next_account_number
        BankAccount.next_account_number += 1

    def add_transaction(self, t):
        self.transactions.append(t)

    def print_statement(self):
        print('Statement')
        print('---------')
        print('\n'.join(self.transactions))
        print('Current balance: {:.2f}'.format(self.balance))

    def lodge(self, amt):
        self.balance += amt
        self.add_transaction('Lodgement: {:.2f}'.format(amt))

    def __str__(self):
        ret = 'Name: {}'.format(self.name)
        ret += '\nAccount number: {}'.format(self.account_number)
        ret += '\nBalance: {:.2f}'.format(self.balance)
        return ret


class CurrentAccount(BankAccount):
    overdraft = 2000.00
    account_type = 'Current account'

    def withdraw(self, amt):
        if amt > self.balance + self.overdraft:
            print('Insufficient funds available')
        else:
            self.balance -= amt
            self.add_transaction('Withdrawal: {:.2f}'.format(amt))

    def __str__(self):
        ret = self.account_type + '\n'
        ret += super().__str__()
        return ret


class SavingsAccount(BankAccount):
    interest_rate = 0.05
    account_type = 'Savings account'

    def apply_interest(self):
        self.add_transaction('Interest: {:.2f}'.format(self.balance*self.interest_rate))
        self.balance *= (1 + self.interest_rate)

    def withdraw(self, amt):
        if amt > self.balance:
            print('Insufficient funds available')
        else:
            self.balance -= amt
            self.add_transaction('Withdrawal: {:.2f}'.format(amt))

    def __str__(self):
        ret = self.account_type + '\n'
        ret += super().__str__()
        return ret
