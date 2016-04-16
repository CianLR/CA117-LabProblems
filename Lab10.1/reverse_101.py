def reverse_list(l):
    if len(l) == 0:
        return []
    else:
        return [l[-1]] + reverse_list(l[:-1])
