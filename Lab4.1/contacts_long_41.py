import sys

phonebook = {}
for line in open(sys.argv[1]):
    name, number, email = line.strip().split(' ')
    phonebook[name] = [number,email]

for i,line in enumerate(sys.stdin):
    line = line.strip()
    if line in phonebook:
        print("Phone: " + phonebook[line][0])
        print("Email: " + phonebook[line][1])
    else:
        print('No such contact')


