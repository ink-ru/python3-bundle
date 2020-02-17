#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Script description
'''

import os, sys, re
import argparse
import env_file

env_file.load()

VERSION = "0.0.1"
DEBUG = False

def createParser (): # http://jenyay.net/Programming/Argparse
	parser = argparse.ArgumentParser(
				prog = sys.argv[0],
				description = '''Pyhton3 script bundle''',
				epilog = '''george.a.wise@gmail.com'''
				)
	parser.add_argument ('-v', '-verbose', required=False, default='0', help = 'Verbose output')
 
	return parser

def main(argv):
    parser = createParser()
	namespace = parser.parse_args()
    mode = namespace.v # sys.argv[1]
    
    pass

sys.exit(os.EX_OK) # code 0, all ok

# assert __name__ is '__main__'
if __name__ == '__main__':
	# main(argv)
	main(sys.argv)
else:
	sys.exit(os.EX_USAGE) # https://docs.python.org/2/library/os.html
