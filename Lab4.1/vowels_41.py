import sys

word_freq = {}
for word in sys.stdin.read():
    word = word.lower()

    if word in 'aeiou':
        word_freq[word] = word_freq[word]+1 if word in word_freq else 1

largest = None
for word, freq in sorted(word_freq.items(), key=lambda x:x[1], reverse=True):
    if largest == None:
        largest = len(str(freq))
    
    print('{} : {:>{}}'.format(word, freq, largest))

    
