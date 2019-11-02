from numpy.random import choice
import pickle

BEGIN = 1
END = 2

model = pickle.load(open("model.pickle", "rb"))

# TODO: try to get consistent lengths - steer away from titles ending super quickly, steer towards line ends when we get too long
# should cut off titles that are too long at some point

def find_next_word(model, prev_word):
  if not prev_word in model or len(model[prev_word]) < 1:
    return END

  targets = []
  probabilities = []

  for target in model[prev_word]:
    targets.append(target)
    probabilities.append(model[prev_word][target])

  draw = choice(targets, 1, p=probabilities)[0]
  return draw

def generate_chain(model):
  draw = BEGIN
  count = 0
  sentence = ''
  while draw != END and count < 30:
    draw = find_next_word(model, draw)
    print(f'draw: {draw}')
    print(type(draw))
    sentence += draw + ' '
    count += 1

  print(sentence)

generate_chain(model)