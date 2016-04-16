import sys

phonebook = {}
for line in open(sys.argv[1]):
    name, number = line.strip().split(' ')
    phonebook[name] = number

for i,line in enumerate(sys.stdin):
    line = line.strip()
    if line in phonebook:
        print("Phone: " + phonebook[line])
    else:
        print('No such contact')


