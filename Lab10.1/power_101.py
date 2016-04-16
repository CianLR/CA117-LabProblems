def power(n, p):
    if p == 0:
        return 1
    else:
        return power(n, p - 1) * n
