#!/usr/bin/env python

import src.markov as markov
from markov import MarkovChain
import loadMidi
import writeMidi
import convert

from . import args


class MarkovMusic:

    def __init__(self):
        self.args = args

    def run(self):
        fileload, resolution, format = loadMidi.load('midi/test.mid')
        #print fileload
        for note in fileload:
            print note.val, note.len, note.pos

        writeMidi.writeList(fileload, resolution, format)

        # print loadMidi.load('midi/bach.mid')

        # mc = MarkovChain(10)
        # mc.add_file('book.txt')
        # while (True):
        #     str = raw_input('\npress enter to generate new text')
        #     print str
        #     print(' '.join(mc.generate_text()) + '.')
