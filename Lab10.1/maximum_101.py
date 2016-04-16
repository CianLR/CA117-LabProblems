def maximum(l):
    if len(l) == 1:
        return l[0]
    else:
        max_ret = maximum(l[1:])
        return l[0] if l[0] > max_ret else max_ret
