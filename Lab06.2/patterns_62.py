import sys
import re

patterns = ' '.join([line[:-1] for line in sys.stdin])

dates1 = re.compile('\d{1,2}/\d{1,2}/\d{1,2}')
dates2 = re.compile('\d{1,2}-\d{1,2}-\d{1,2}')
dates3 = re.compile('\d{1,2}[-/]\d{1,2}[-/]\d{1,2}')
phones = re.compile('01[- ][0-9]{7}')
emails = re.compile('\w+(?:\.\w+)*@\w+(?:\.\w+)+')
dates4 = re.compile('\d{1,2} [A-Z]\w{2} \d{2,4}')

print(dates1.findall(patterns))
print(dates2.findall(patterns))
print(dates3.findall(patterns))
print(phones.findall(patterns))
print(emails.findall(patterns))
print(dates4.findall(patterns))

