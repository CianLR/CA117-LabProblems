import sys

def main():
    punctuation = '\',.?!": \n'
    for line in sys.stdin.readlines():
        for c in punctuation:
            line = line.replace(c, '')
        line = line.lower()
        
        print(line == line[::-1])

if __name__ == '__main__':
    main()
