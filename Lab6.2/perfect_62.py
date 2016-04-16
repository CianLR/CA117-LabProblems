import sys

def sumFac(n):    
    factor_sum = 0
    i = 1
    while i < n:
        if n%i == 0:
            factor_sum += i

        i += 1

    return factor_sum

def isPerfect(n):
    return n == sumFac(n)

for line in sys.stdin:
    x = int(line)
    print(isPerfect(x))
    
