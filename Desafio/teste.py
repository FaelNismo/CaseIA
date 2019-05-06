from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

exemplo = 'Isso é um exemplo de como as tecnicas de tratamento de Stopwords e Tokenização funcionam '
word = word_tokenize(exemplo)
print(word)
stop_word = set(stopwords.words("portuguese"))
sentenca_feita = []

for w in word:
	if w not in stop_word:
		sentenca_feita.append(w)
print(sentenca_feita)