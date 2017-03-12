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
        fileload, resolution, format = loadMidi.load('midi/bach_simple.mid')
        # print fileload
        for note in fileload:
            print note.val, note.len, note.pos

        stringNotes = convert.listToString(fileload)

        mc = MarkovChain(1)
        mc.add_string(stringNotes)
        markovNotes = ' '.join(mc.generate_text(50))
        print stringNotes
        print mc.generate_text()
        writeMidi.writeList(convert.stringToList(markovNotes), resolution, format)

        # while (True):
        #     str = raw_input('\npress enter to generate new text')
        #     print str
        #     print(' '.join(mc.generate_text()) + '.')
