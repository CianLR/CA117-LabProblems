class Employee(object):
    next_employee_number = 1

    def __init__(self, forename, surname, ssn):
        self.forename = forename
        self.surname = surname
        self.ssn = ssn
        self.employee_number = self.next_employee_number
        Employee.next_employee_number += 1

    def __str__(self):
        ret_string = []
        ret_string.append('Name: {} {}'.format(self.forename, self.surname))
        ret_string.append('SSN: {}'.format(self.ssn))
        ret_string.append('Number: {}'.format(self.employee_number))
        return '\n'.join(ret_string)


class SalariedEmployee(Employee):
    employee_type = 'Salaried'
    tax_rate = 0.2
    
    def __init__(self, forename, surname, ssn, salary):
        self.salary = float(salary)
        super().__init__(forename, surname, ssn)

    def earnings(self):
        return self.salary * (1 - self.tax_rate)

    def __str__(self):
        ret_string = []
        ret_string.append('Type: {}'.format(self.employee_type))
        ret_string.append(super().__str__())
        ret_string.append('Earnings: {:.2f}'.format(self.earnings()))
        return '\n'.join(ret_string)


class HourlyEmployee(Employee):
    employee_type = 'Hourly'
    tax_rate = 0.1
    
    def __init__(self, forename, surname, ssn, hourly_rate, hours):
        self.hourly_rate = float(hourly_rate)
        self.hours = float(hours)
        super().__init__(forename, surname, ssn)

    def earnings(self):
        return self.hourly_rate * self.hours * (1 - self.tax_rate)

    def __str__(self):
        ret_string = []
        ret_string.append('Type: {}'.format(self.employee_type))
        ret_string.append(super().__str__())
        ret_string.append('Earnings: {:.2f}'.format(self.earnings()))
        return '\n'.join(ret_string)


class CommissionEmployee(Employee):
    employee_type = 'Commission'
    tax_rate = 0.05
    
    def __init__(self, forename, surname, ssn, sales, commission_rate):
        self.sales = float(sales)
        self.commission_rate = float(commission_rate) / 100
        super().__init__(forename, surname, ssn)

    def earnings(self):
        return self.sales * self.commission_rate * (1 - self.tax_rate)

    def __str__(self):
        ret_string = []
        ret_string.append('Type: {}'.format(self.employee_type))
        ret_string.append(super().__str__())
        ret_string.append('Earnings: {:.2f}'.format(self.earnings()))
        return '\n'.join(ret_string)
