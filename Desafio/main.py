from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import  SnowballStemmer

stem = SnowballStemmer('portuguese')
with open('texto.txt', 'rb') as f:
	text = f.read()

def procura(query):
	for sent in sent_tokenize(text.decode('utf8')):
		for token in word_tokenize(sent):

			if query in sent:
				return sent
			else:
				continue 
	return

while True:
	q = input('Entre com uma busca: ')
	print (procura (q))
print(stem.stem(q))

	