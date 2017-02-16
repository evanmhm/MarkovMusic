#!/usr/bin/env python

import src.markov as markov
from markov import MarkovChain
import loadMIDI

from . import args

class MarkovMusic:
    def __init__(self):
        self.args = args

    def run(self):
        loadMIDI.testWrite()
        mc = MarkovChain(10)
        mc.add_file('bible.txt')
        while (True):
            str = raw_input('\npress enter to generate new text')
            print str
            print(' '.join(mc.generate_text()) + '.')
