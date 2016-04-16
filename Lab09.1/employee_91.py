class Employee:
    def __init__(self, name, number):
        self.name = name
        self.number = number

    def wages(self):
        return 0

    def __str__(self):
        return 'Name: {}\nNumber: {}\nWages: {:.2f}'.format(
            self.name,
            self.number,
            self.wages()
            )


class Manager(Employee):
    def __init__(self, name, number, salary):
        self.salary = salary
        super().__init__(name, number)

    def wages(self):
        return self.salary / 52


class AssemblyWorker(Employee):
    def __init__(self, name, number, hourly_rate, hours):
        self.hourly_rate = hourly_rate
        self.hours = hours
        super().__init__(name, number)

    def wages(self):
        return hourly_rate * hours
