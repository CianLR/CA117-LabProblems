import sys

wordlist = []
for word in sys.stdin:
    wordlist.append(word[:-1])

print('Words containing 17 letters:',[x for x in wordlist if len(x)==17])
print('Words containing 18+ letters:',[x for x in wordlist if len(x)>17])
all_vowels = [x for x in wordlist if len(set(x.lower())&set('aeiou'))==5]
print('Shortest word containing all vowels:',sorted(all_vowels,key=lambda x:len(x))[0])
print('Words with 4 a\'s:',[x for x in wordlist if x.lower().count('a')==4])
print('Words with 2+ q\'s:',[x for x in wordlist if x.lower().count('q')>1])
print('Words containing cie:',[x for x in wordlist if 'cie' in x.lower()])
print('Anagrams of angle:',[x for x in wordlist if len(x)==5 and set(x.lower())==set('angle') and x!='angle'])
print('Words ending in iary:',len([x for x in wordlist if len(x)>3 and x[-4:]=='iary']))
print('Words with q but no u:',[x for x in wordlist if 'q' in x.lower() and 'u' not in x.lower()])
e_count = sorted([(x.lower().count('e'),x) for x in wordlist],key=lambda x:x[0], reverse=True)
print('Words with most e\'s:',[x[1] for x in e_count if x[0] == e_count[0][0]])

