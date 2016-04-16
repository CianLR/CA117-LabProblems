import sys

def main():
    size = int(sys.argv[1])
    
    for i in range(2*size):
        spaces = abs(i-size)
        print(' '*spaces + '* '*(size-spaces))
        
    
if __name__ == '__main__':
    main()
