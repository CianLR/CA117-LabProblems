import sys

def main():
    char_list, test_string = sys.argv[1:]
    
    for c in char_list:
        if c in test_string:
            test_string = test_string.replace(c,'',1)
        else:
            print('False')
            return

    print('True')
    return

if __name__ == '__main__':
    main()
