#!/usr/bin/env python

import src.markov as markov
from markov import MarkovChain

from . import args

class MarkovMusic:
    def __init__(self):
        self.args = args

    def run(self):
        mc = MarkovChain(10)
        mc.add_file('book.txt')
        print(' '.join(mc.generate_text()) + '.')
