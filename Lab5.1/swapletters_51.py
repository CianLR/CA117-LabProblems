import sys

def swap(s):
    end_char = ''
    if len(s)%2:
        end_char = s[-1]
    
    i = 0
    swapped = ''
    while i < len(s) - 1:
        swapped += s[i+1] + s[i]
        i += 2

    return swapped + end_char

if __name__ == '__main__':
    print(swap(sys.argv[1]))
