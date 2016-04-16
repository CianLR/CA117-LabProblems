from collections import namedtuple

Student = namedtuple('Student',['firstname','surname','id'])

def show_student(s):
    print('First name:',s.firstname)
    print('   Surname:',s.surname)
    print('        ID:',s.id)
