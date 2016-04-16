import sys


def main():
        word = sys.argv[1]
        out_word = ''

        for i in range(0, len(word)-1, 2):
                out_word += word[i+1] + word[i]

        if len(word) % 2:
                out_word += word[-1]

        print(out_word)

if __name__ == '__main__':
        main()
