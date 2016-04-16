import sys, string

word_freq = {}
for word in sys.stdin.read().split():
    word = word.lower().strip(string.punctuation)

    if len(word) > 3:
        word_freq[word] = word_freq[word]+1 if word in word_freq else 1

for word, freq in sorted(word_freq.items()):
    if freq > 2:
        print(word + ' : ' + str(freq))

    
