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

transitions = {}
transitions[BEGIN] = {}
totals = {}
totals[BEGIN] = 0

# count all the occurrences of certain transitions
for tagline in taglines:
  # TODO: can keep track of most common original form of word - for example, John -> john
  line = tokenizer.tokenize(tagline)
  line = [word.lower() for word in line]
  if len(line) < 1:
    continue

  transitions[BEGIN][line[0]] = transitions[BEGIN].get(line[0], 0) + 1
  totals[BEGIN] += 1

  for i in range(len(line)):
    transition_dict = transitions.get(line[i], {})
    next_token = line[i + 1] if i < len(line) - 1 else END
    transition_dict[next_token] = transition_dict.get(next_token, 0) + 1
    transitions[line[i]] = transition_dict
    totals[line[i]] = totals.get(line[i], 0) + 1

# print(transitions)

model = {}

# normalize probabilities
for key in transitions:
  model[key] = {}
  for target in transitions[key]:
    model[key][target] = transitions[key][target] / totals[key]

# print(model)

pickle.dump(model, open('model.pickle', 'wb'))