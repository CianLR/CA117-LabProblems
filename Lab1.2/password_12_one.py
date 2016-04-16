import sys, string

password = frozenset(sys.argv[1])
chr_classes = [
    frozenset(string.ascii_uppercase),
    frozenset(string.ascii_lowercase),
    frozenset(string.digits),
    frozenset(string.punctuation),
    ]

strength = 0
for class_set in chr_classes:
    if class_set.intersection(password):
        strength += 1

print(strength)

