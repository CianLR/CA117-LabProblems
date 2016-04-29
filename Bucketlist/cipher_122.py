import sys

def c2o(letter):
	return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'.find(letter)

def o2c(letter):
	return 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'[letter]

def main():

	cypher_text = sys.stdin.read()

	alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
	most_common = ''
	most_common_num = 0

	for c in alphabet:
		freq = cypher_text.count(c)
		if freq > most_common_num:
			most_common_num = freq
			most_common = c

	shift = c2o(most_common) - c2o('E') #Assume most common is 'e'

	for c in cypher_text:
		if c in alphabet:
			print(o2c( (c2o(c)-c2o('A')-shift)%len(alphabet) ), end='')
		else:
			print(c, end='')


if __name__ == '__main__':
	main()