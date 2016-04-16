from math import pi
import sys

def area(radius):
    return 4*pi*(radius**2)

def volume(radius):
    return (4/3)*pi*(radius**3)

def main():
    print('Radius (m)      Area (m^2)    Volume (m^3)\n'
          '----------      ----------    ------------')
    *_, start, step, end = sys.argv

    counter = float(start)
    while counter <= float(end):
        print('{:>10.1f}'.format(counter)+
              '      '+
              '{:>10.2f}'.format(area(counter))+
              '    '+
              '{:>12.2f}'.format(volume(counter)))
        counter += float(step)

if __name__ == '__main__':
    main()
