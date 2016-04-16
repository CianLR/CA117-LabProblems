from sys import argv
import calendar

poem = ['Monday\'s child is fair of face.',
        'Tuesday\'s child is full of grace.',
        'Wednesday\'s child is full of woe.',
        'Thursday\'s child has far to go.',
        'Friday\'s child is loving and giving.',
        'Saturday\'s child works hard for a living.',
        'Sunday\'s child is fair and wise and good in every way.']

day, month, year = int(argv[1]), int(argv[2]), int(argv[3])
day_of_birth = calendar.weekday(year,month,day)

print('You were born on a',poem[day_of_birth][:poem[day_of_birth].find('\'')],'and',poem[day_of_birth])
