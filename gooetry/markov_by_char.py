import markov

class CharacterMarkovGenerator(markov.MarkovGenerator):
	def tokenize(self, text):
		return list(text)
	def concatenate(self, source):
		return ''.join(source)

if __name__ == '__main__':

	import sys

	# set numbers
	generator = CharacterMarkovGenerator(n=9, max=200)
	lines = set()
	for line in sys.stdin:
		line = line.strip()
		generator.feed(line)

	# number of chunks to return		
	for i in range(3):
		print generator.generate()

