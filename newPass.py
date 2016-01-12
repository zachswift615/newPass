import string


class NewPass(object):

	def __init__(self, phrase):
		self.phrase = phrase
		self.translate = {
			'i': '!', 
			'a': '4',
			'b': '8',
			'o': '0',
			'e': '3',
			's': '5',
			'x': '%',
			'g': '9',

		}

	def hackronym(self):
		ret = ""
		for word in phrase.lower().split():
			try:
				ret += self.translate[word[0]]
			except KeyError:
				ret += word[0]
		ret = list(ret)		
		for i in range(1, len(phrase.split()), 2):
			ret[i] = ret[i].upper()
		if not any([letter in string.punctuation or letter in string.digits for letter in ret]):
			ret.append('!')
		return ''.join(ret)
			
if __name__ == "__main__":
	phrase = input('Phrase to bass password off of: ')
	n = NewPass(phrase)
	print(n.hackronym())

