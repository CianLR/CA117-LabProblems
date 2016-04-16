class Element:
    def __init__(self, number, name, symbol, b_p):
        self.number = number
        self.name = name
        self.symbol = symbol
        self.b_p = b_p

    def print_details(self):
        print("Number:",self.number)
        print("Name:",self.name)
        print("Symbol:",self.symbol)
        print("Boiling point:",self.b_p, "C")
