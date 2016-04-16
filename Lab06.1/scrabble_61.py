import sys


def all_common(word, letter_set):
    for c in word:
        if c in letter_set:
            letter_set = letter_set.replace(c, '', 1)
        else:
            return False

    return True


def score(word):
    tile_values = {
        'a': 1, 'f': 4, 'k': 5, 'p': 3, 'u': 1,
        'z': 10, 'b': 3, 'c': 3, 'd': 2, 'e': 1,
        'g': 2, 'h': 4, 'i': 1, 'j': 8,
        'l': 1, 'm': 3, 'n': 1, 'o': 1,
        'q': 10, 'r': 1, 's': 1, 't': 1,
        'v': 4, 'w': 4, 'x': 8, 'y': 4,
        }
    return sum([tile_values[c] for c in word])


def main():
    available = sys.argv[1]

    best_word = ''
    best_score = 0
    for line in sys.stdin:
        line = line[:-1]

        if not all_common(line, available):
            continue

        if score(line) > best_score:
            best_score = score(line)
            best_word = line

    print(best_word+': '+str(best_score))

if __name__ == '__main__':
    main()
