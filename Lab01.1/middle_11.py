import sys

def main():
    test_string = sys.argv[1]
    if len(test_string)%2 == 0:
        print('No middle character!')
    else:
        mid = len(test_string)//2
        print(test_string[mid])

if __name__ == '__main__':
    main()
