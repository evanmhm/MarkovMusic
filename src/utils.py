#!/usr/bin/env python

import sys
import os
import configargparse


def get_args():
	default_config = []

	if '-cf' not in sys.argv and '--config' not in sys.argv:
		default_config = [os.getenv('MARKOV_CONFIG', os.path.join(os.path.dirname(__file__), '../config/config.ini'))]

	parser = configargparse.ArgParser(default_config_files=default_config, auto_env_var_prefix='NEURAL')

	parser.add_argument("-v", "--verbose", action="store_true", help="for debugging, prints useful values")

	return vars(parser.parse_args())
