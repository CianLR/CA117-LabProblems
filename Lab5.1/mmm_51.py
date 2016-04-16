import sys

def mean(l):
    return sum(l) / len(l)

def mode(l):
    return max(l, key=l.count)

def median(l):
    size = len(l)
    if size%2:
        return l[size//2]
    else:
        return (l[size//2] + l[(size//2)-1])/2

def main():
    l = sorted([int(x) for x in sys.stdin])
    print('Mean: {:.1f}'.format(mean(l)))
    print('Mode: {:.1f}'.format(mode(l)))
    print('Median: {:.1f}'.format(median(l)))
    
if __name__ == '__main__':
    main()
