import sys
from datetime import time as timeOBJ

def main():
    best_name = ''
    best_time = None
    for line in sys.stdin:
        name, *time_str = line.split()
        times = []
        for time in time_str:
            try:
                mins = int(time.split(':')[0])
                secs = int(time.split(':')[1])
                times.append(timeOBJ(0,mins,secs))
            except:
                times = []
                break

        if best_time == None:
            best_time = min(times, default=best_time)
            best_name = name
        elif best_time > min(times, default=best_time):
            best_time = min(times, default=best_time)
            best_name = name

    print('{} : {}:{:02}'.format(best_name,best_time.minute,best_time.second))

if __name__ == '__main__':
          main()
