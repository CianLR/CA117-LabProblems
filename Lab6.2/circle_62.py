
def overlap(x1=0, y1=0, r1=1, x2=0, y2=0, r2=1):
    dist = ( (x1-x2)**2 + (y1-y2)**2 )**0.5
    return dist < r1 + r2
    
