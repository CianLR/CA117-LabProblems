print(len(set(''.join(x for x in __import__('sys').stdin.read().lower()if x not in __import__('string').punctuation).split())))
