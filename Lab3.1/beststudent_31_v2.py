import sys

def get_best():
    f = open(sys.argv[1])
    b_mark = 0
    b_student = ''

    for line in f.readlines():
        m = line[:line.find(' ')]
        try:
            m = int(m)
        except:
            print("Invalid mark",m,"encountered. Exiting.")
            sys.exit()
        
        s = line[line.find(' ')+1:-1]

        if m > b_mark:
            b_mark = m
            b_student = s

    print("Best student:", b_student)
    print("Best mark:", b_mark)

if __name__ == '__main__':
    get_best()
