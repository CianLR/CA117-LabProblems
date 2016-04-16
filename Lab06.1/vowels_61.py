import sys


def main():
    vowels = 'aeiou'

    for line in sys.stdin:
        v_found = [False]*len(vowels)
        print_word = True

        for c in line.lower():
            if c not in vowels:
                continue

            c_order = vowels.find(c)
            if any(v_found[c_order:]):
                print_word = False
                break

            v_found[c_order] = True

        if print_word and all(v_found):
            print(line[:-1])


if __name__ == '__main__':
    main()
