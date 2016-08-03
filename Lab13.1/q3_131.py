class Weight(object):

    OUNCES_PER_POUND = 16
    
    def __init__(self, pounds=0, ounces=0):
        # This handles cases when ounces > 16 or < 0
        self.p = pounds + (ounces // self.OUNCES_PER_POUND)
        self.o = ounces % self.OUNCES_PER_POUND

    def to_ounces(self):
        return (self.p * self.OUNCES_PER_POUND) + self.o

    def __str__(self):
        return '{} pound(s) and {} ounce(s)'.format(self.p, self.o)

    def __eq__(self, other):
        return self.to_ounces() == other.to_ounces()

    def __ne__(self, other):
        return not self == other

    def __gt__(self, other):
        return self.to_ounces() > other.to_ounces()

    def __ge__(self, other):
        return (self == other) or (self > other)

    def __lt__(self, other):
        return self.to_ounces() < other.to_ounces()

    def __le__(self, other):
        return (self == other) or (self < other)

    def __add__(self, other):
        return Weight(self.p + other.p,
                      self.o + other.o)

    def __iadd__(self, other):
        self.p, self.o = divmod(self.to_ounces() + other.to_ounces(),
                                self.OUNCES_PER_POUND)
        return self

    def __mul__(self, other):
        # Note the flatten operator (*) before divmod
        return Weight(*divmod(self.to_ounces() * other,
                              self.OUNCES_PER_POUND))

    def __imul__(self, other):
        self.p, self.o = divmod(self.to_ounces() * other,
                                self.OUNCES_PER_POUND)
        return self

    def __rmul__(self, other):
        # Calls __mul__
        return self * other

    def __sub__(self, other):
        return Weight(0, self.to_ounces() - other.to_ounces())

    def __isub__(self, other):
        self.p, self.o = divmod(self.to_ounces() - other.to_ounces(),
                                self.OUNCES_PER_POUND)
        return self

    @staticmethod
    def from_ounces(ounces):
        return Weight(0, ounces)
