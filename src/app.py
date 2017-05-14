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
        print ("Loading input and generating...")
        fileload, resolution, format = loadMidi.load('midi/bach_simple.mid')

        stringNotes = convert.listToString(fileload)

        mc = MarkovChain(1)
        mc.add_string(stringNotes)
        markovNotes = ' '.join(mc.generate_text(50))

        writeMidi.writeList(convert.stringToList(markovNotes), resolution, format)
        print ('Process complete, output is in ./rebuilt.mid')
