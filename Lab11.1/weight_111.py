class Weight:

    OUNCES_PER_POUND = 16

    def __init__(self, pounds=0, ounces=0):
        self.pounds = pounds
        self.ounces = ounces

    def to_ounces(self):
        return (self.pounds * self.OUNCES_PER_POUND) + self.ounces

    def __str__(self):
        return '{} pound(s) and {} ounce(s)'.format(self.pounds, self.ounces)

    def __eq__(self, other):
        return (self.pounds, self.ounces) == (other.pounds, other.ounces)

    def __ne__(self, other):
        return (self.pounds, self.ounces) != (other.pounds, other.ounces)

    def __gt__(self, other):
        return (self.pounds, self.ounces) > (other.pounds, other.ounces)

    def __lt__(self, other):
        return (self.pounds, self.ounces) < (other.pounds, other.ounces)

    def __ge__(self, other):
        return (self.pounds, self.ounces) >= (other.pounds, other.ounces)

    def __le__(self, other):
        return (self.pounds, self.ounces) <= (other.pounds, other.ounces)

    def __eq__(self, other):
        return (self.pounds, self.ounces) == (other.pounds, other.ounces)

    def __add__(self, other):
        p, o = divmod(self.to_ounces() + other.to_ounces(), self.OUNCES_PER_POUND)
        return Weight(p, o)

    def __iadd__(self, other):
        self.pounds, self.ounces = divmod(self.to_ounces() + other.to_ounces(), self.OUNCES_PER_POUND)
        return self

    def __radd__(self, other):
        p, o = divmod(self.to_ounces() + other.to_ounces(), self.OUNCES_PER_POUND)
        return Weight(p, o)

    def __sub__(self, other):
        p, o = divmod(self.to_ounces() - other.to_ounces(), self.OUNCES_PER_POUND)
        if p < 0:
            return Weight(0, 0)
        return Weight(p, o)

    def __isub__(self, other):
        self.pounds, self.ounces = divmod(self.to_ounces() - other.to_ounces(), self.OUNCES_PER_POUND)
        if self.pounds < 0:
            self.pounds = self.ounces = 0
            return self
        return self

    def __rsub__(self, other):
        p, o = divmod(self.to_ounces() - other.to_ounces(), self.OUNCES_PER_POUND)
        if p < 0:
            return Weight(0, 0)
        return Weight(p, o)

    def __mul__(self, other):
        p, o = divmod(self.to_ounces() * other, self.OUNCES_PER_POUND)
        return Weight(p, o)

    def __imul__(self, other):
        self.pounds, self.ounces = divmod(self.to_ounces() * other, self.OUNCES_PER_POUND)
        return self

    def __rmul__(self, other):
        p, o = divmod(self.to_ounces() * other, self.OUNCES_PER_POUND)
        return Weight(p, o)

    @classmethod
    def from_ounces(cls, ounces):
        return cls(*divmod(ounces, cls.OUNCES_PER_POUND))
