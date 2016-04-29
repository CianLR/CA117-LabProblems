class Distance:
    YARDS_PER_MILE = 1760

    def __init__(self, miles=0, yards=0):
        self.m = miles + yards//self.YARDS_PER_MILE
        self.y = yards%self.YARDS_PER_MILE

    def __str__(self):
        return '{} mile(s) and {} yard(s)'.format(self.m, self.y)

    @classmethod
    def from_yards(cls, yards):
        return cls(0, yards)

    def to_yards(self):
        return (self.m * self.YARDS_PER_MILE) + self.y

    def __eq__(self, other):
        return self.to_yards() == other.to_yards()

    def __gt__(self, other):
        return self.to_yards() > other.to_yards()

    def __lt__(self, other):
        return self.to_yards() < other.to_yards()

    def __ge__(self, other):
        return self.to_yards() >= other.to_yards()

    def __le__(self, other):
        return self.to_yards() <= other.to_yards()

    def __add__(self, other):
        return Distance(0, self.to_yards() + other.to_yards())

    def __iadd__(self, other):
        self.m, self.y = divmod(self.to_yards()+other.to_yards(), self.YARDS_PER_MILE)
        return self

    def __sub__(self, other):
        return Distance(0, self.to_yards() - other.to_yards())

    def __mul__(self, other):
        return Distance(0, self.to_yards() * other)

    def __rmul__(self, other):
        return self.__mul__(other)
