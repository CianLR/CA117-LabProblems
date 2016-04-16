class Score:
    def __init__(self, goals=0, points=0):
        self.goals = goals
        self.points = points

    def less_than(self, s2):
        return (self.points + self.goals*3) < (s2.points + s2.goals*3)

    def greater_than(self, s2):
        return (self.points + self.goals*3) > (s2.points + s2.goals*3)

    def equal_to(self, s2):
        return (self.points + self.goals*3) == (s2.points + s2.goals*3)
