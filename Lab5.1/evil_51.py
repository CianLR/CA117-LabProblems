import sys, re

def evil_check():
    EVIL = 'evil'

    for line in sys.stdin:
        e_index = 0

        right_count = True

        for c in EVIL:
            if not line.lower().count(c) == 1:
                right_count = False
                break

        if not right_count:
            continue
        
        for c in line.lower():
            if c == EVIL[e_index]:
                e_index += 1

            if e_index == len(EVIL):
                print(line[:-1])
                break

if __name__ == '__main__':
    evil_check()
