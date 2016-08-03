import sys

def main():
    freq_dict = {}
    for word in sys.stdin.read().split():
        word = ''.join(
            [c for c in word.lower() if c.isalpha() or c == "'"]
        )
        if word == '':
            continue

        if word in freq_dict:
            freq_dict[word] += 1
        else:
            freq_dict[word] = 1

    for word in sorted(freq_dict):
        print(word, ':', freq_dict[word])

if __name__ == '__main__':
    main()
