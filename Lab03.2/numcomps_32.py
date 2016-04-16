
list30 = []
for i in range(1,31):
    list30.append(i)

print("Multiples of 3:",[x for x in list30 if x%3==0])
print("Multiples of 3 squared:",[x**2 for x in list30 if x%3==0])
print("Multiples of 4 doubled:",[x*2 for x in list30 if x%4==0])
print("Multiples of 3 or 4:",[x for x in list30 if x%3==0 or x%4==0])
print("Multiples of 3 and 4:",[x for x in list30 if x%3==0 and x%4==0])
print("Multiples of 3 replaced:",[x if not x%3==0 else 'X' for x in list30])
