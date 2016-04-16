import sys

def end_capital(s):
    return s[0].upper() + s[1:-1] + s[-1].upper()

def main():
    lower_input = sys.argv[1]
    if len(lower_input) > 1:
        print(end_capital(lower_input))

if __name__ == '__main__':
    main()
