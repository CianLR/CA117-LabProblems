class Point:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def reflect(self):
        self.x = -self.x
        self.y = -self.y

    def distance(self, point2):
        return ( (self.x - point2.x)**2 + (self.y - point2.y)**2 )**0.5
        

    
