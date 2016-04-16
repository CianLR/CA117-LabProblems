class Employee:

    next_employee_number = 1

    def __init__(self, forename, surname, ssn):
        self.forename = forename
        self.surname = surname
        self.ssn = ssn
        self.employee_number = Employee.next_employee_number
        Employee.next_employee_number += 1

    def __str__(self):
        ret = 'Name: {} {}\n'.format(self.forename, self.surname)
        ret += 'SSN: {}\n'.format(self.ssn)
        ret += 'Number: {}'.format(self.employee_number)
        return ret


class SalariedEmployee(Employee):

    tax_rate = 0.2
    employee_type = "Salaried"

    def __init__(self, forename, surname, ssn, salary):
        super().__init__(forename, surname, ssn)
        self.salary = salary

    def earninigs(self):
        return self.salary * (1 - self.tax_rate)

    def __str__(self):
        ret = 'Type: {}\n'.format(self.employee_type)
        ret += super().__str__() + '\n'
        ret += 'Earnings: {:.2f}'.format(self.earninigs())
        return ret


class HourlyEmployee(Employee):

    tax_rate = 0.1
    employee_type = "Hourly"

    def __init__(self, forename, surname, ssn, hourly_rate, hours):
        super().__init__(forename, surname, ssn)
        self.hourly_rate = hourly_rate
        self.hours = hours

    def earninigs(self):
        return self.hours * self.hourly_rate * (1 - self.tax_rate)

    def __str__(self):
        ret = 'Type: {}\n'.format(self.employee_type)
        ret += super().__str__() + '\n'
        ret += 'Earnings: {:.2f}'.format(self.earninigs())
        return ret


class CommissionEmployee(Employee):

    tax_rate = 0.05
    employee_type = "Commission"

    def __init__(self, forename, surname, ssn, sales, commission_rate):
        super().__init__(forename, surname, ssn)
        self.sales = sales
        self.commission_rate = commission_rate

    def earninigs(self):
        return self.sales * (self.commission_rate/100) * (1 - self.tax_rate)

    def __str__(self):
        ret = 'Type: {}\n'.format(self.employee_type)
        ret += super().__str__() + '\n'
        ret += 'Earnings: {:.2f}'.format(self.earninigs())
        return ret
