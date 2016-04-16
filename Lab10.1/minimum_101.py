def minimum(l):
    if len(l) == 1:
        return l[0]
    else:
        min_ret = minimum(l[1:])
        return l[0] if l[0] < min_ret else min_ret
