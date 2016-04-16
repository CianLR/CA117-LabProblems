import sys

def get_best():
    f = open(sys.argv[1])
    b_mark = 0
    b_students = ''

    for line in f.readlines():
        try:
            m = line[:line.find(' ')]
            m = int(m)
            s = line[line.find(' ')+1:-1]

            if m > b_mark:
                b_mark = m
                b_students = s
            elif m == b_mark:
                b_students += ', ' + s
            
        except:
            print("Invalid mark",m,"encountered. Skipping.")

    print("Best student(s):", b_students)
    print("Best mark:", b_mark)

if __name__ == '__main__':
    get_best()
