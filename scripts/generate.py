from numpy.random import choice
import pickle
import os

class Generator:

  def __init__(self):
    self.BEGIN = '__BEGIN__'
    self.END = '__END__'
    # file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
      # 'tagline-lstm-model.pickle'), "rb")
    # self.tagline_lstm_model = pickle.load(file)
    file = open(os.path.join(os.path.dirname(os.path.abspath(__file__)),
      'tagline-markov-model.pickle'), "rb")
    self.tagline_markov_model = pickle.load(file)


  # TODO: try to get consistent lengths - steer away from titles ending super \
  # quickly, steer towards line ends when we get too long
  # should cut off titles that are too long at some point

  def find_next_word(self, prev_word):
    if not prev_word in self.tagline_markov_model or
    len(self.tagline_markov_model[prev_word]) < 1:
      return END

    targets = []
    probabilities = []

    for target in self.tagline_markov_model[prev_word]:
      targets.append(target)
      probabilities.append(self.tagline_markov_model[prev_word][target])

    draw = choice(targets, 1, p=probabilities)[0]
    return draw

  def generate_chain(self):
    draw = self.BEGIN
    count = 0
    sentence = ''

    while count < 30:
      draw = self.find_next_word(draw)
      if draw == self.END: break
      sentence += draw + ' '
      count += 1

    # print(sentence)
    return sentence

  def generate_tagline(self):
    return self.generate_chain()


# generate_chain(model)