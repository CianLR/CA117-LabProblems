import sys

def main():
    num, base = sys.argv[1:]
    print(int(num,int(base)))
    
if __name__ == '__main__':
    main()
