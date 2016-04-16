import sys


def main():
        names = []
        for line in sys.stdin:
                names.append(line[:-1])

        avg_len = sum(map(len, names))/len(names)
        print('Average: {:.2f}'.format(avg_len))
        print([x for x in names if len(x) > avg_len])

if __name__ == '__main__':
        main()
