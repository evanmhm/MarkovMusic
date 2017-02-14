#!/usr/bin/env python

import src.markov as markov

from . import args

class MarkovMusic:
    def __init__(self):
        self.args = args

    def run(self):
        markov.StartChain(self)
