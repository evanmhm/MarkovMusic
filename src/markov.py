import re, random
from collections import defaultdict, deque

#base markov chain from https://github.com/Codecademy/markov_python

class MarkovChain:

  def __init__(self, key_words=2):
    self.key_words = key_words
    self.lookup_dict = defaultdict(list)
    self._punctuation_regex = re.compile('[.!;\?\:\-\[\]\n]+')
    self._seeded = False
    self.__seed_me()

  def __seed_me(self, rand_seed=None):
    if self._seeded is False:
      try:
        if rand_seed is not None:
          random.seed(rand_seed)
        else:
          random.seed()
        self._seeded = True
      except NotImplementedError:
        self._seeded = False

  def add_file(self, file_path):
    content = ''
    with open(file_path, 'r') as fh:
      self.__add_source_data(fh.read())

  def add_string(self, str):
    self.__add_source_data(str)

  def __add_source_data(self, str):
    clean_str = self._punctuation_regex.sub(' ', str).lower()
    tuples = self.__generate_tuple_keys(clean_str.split())
    for t in tuples:
      self.lookup_dict[t[0]].append(t[1])

  def __generate_tuple_keys(self, data):
    if len(data) < self.key_words:
      return

    for i in xrange(len(data) - self.key_words):
      yield [tuple(data[i:i + self.key_words]), data[i + self.key_words]]

  """
  " Generates text based on the data the Markov Chain contains
  " max_length is the maximum number of words to generate
  """
  def generate_text(self, max_length=20):
    context = deque()
    output = []
    if len(self.lookup_dict) > 0:
      self.__seed_me(rand_seed=len(self.lookup_dict))

      idx = random.randint(0, len(self.lookup_dict)-1)
      chain_head = list(self.lookup_dict.keys()[idx])
      context.extend(chain_head)

      while len(output) < (max_length - self.key_words):
        next_choices = self.lookup_dict[tuple(context)]
        if len(next_choices) > 0:
          next_word = random.choice(next_choices)
          context.append(next_word)
          output.append(context.popleft())
        else:
          break
      output.extend(list(context))
    return output
