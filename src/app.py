#!/usr/bin/env python

import src.markov as markov
from markov import MarkovChain
import loadMidi

from . import args

class MarkovMusic:
    def __init__(self):
        self.args = args

    def run(self):
        print loadMidi.load('midi/test.mid')
        print
        print loadMidi.load('midi/bach.mid')

        # mc = MarkovChain(10)
        # mc.add_file('book.txt')
        # while (True):
        #     str = raw_input('\npress enter to generate new text')
        #     print str
        #     print(' '.join(mc.generate_text()) + '.')
