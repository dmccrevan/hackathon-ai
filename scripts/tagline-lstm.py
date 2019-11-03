import pickle
import nltk
from nltk.tokenize import RegexpTokenizer

tokenizer = RegexpTokenizer(r'\w+')

# import textblob

print('constructing markov chain...')

# titles = pickle.load(open("titles.pickle", "rb"))
taglines = pickle.load(open("taglines.pickle", "rb"))
# print(len(titles))
print(len(taglines))

# taglines = taglines[:30]

BEGIN = '__BEGIN__'
END = '__END__'

model = {}



pickle.dump(model, open('tagline-lstm-model.pickle', 'wb'))
