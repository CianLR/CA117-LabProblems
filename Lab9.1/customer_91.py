class Customer:
    discount = 0

    def __init__(self, name, bal, addr1, addr2, addr3):
        self.name = name
        self.bal = bal
        self.addr = '\n' + '\n'.join([addr1, addr2, addr3])

    def owes(self):
        return self.bal * (1 - self.discount/100)

    def __str__(self):
        ret_str = self.name
        ret_str += self.addr
        ret_str += '\nBalance: {:.2f}\nDiscount: {}%\nAmount due: {:.2f}'.format(
            self.bal,
            self.discount,
            self.owes())
        return ret_str


class ValuedCustomer(Customer):
    discount = 10
