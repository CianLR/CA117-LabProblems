import sys

months = {
    'January':1,
    'February':2,
    'March':3,
    'April':4,
    'May':5,
    'June':6,
    'July':7,
    'August':8,
    'September':9,
    'October':10,
    'November':11,
    'December':12,
    }

for line in sys.stdin:
    day_in, month_in, year_in = line.split()
    print(day_in+'/'+str(months[month_in])+'/'+year_in[2:])
    
