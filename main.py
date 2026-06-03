#!/usr/bin/python3
# -*- coding: utf-8 -*-

'''
Script description: Empty python boilerplate skeleton wireframe template to start a new Python3 project from the scratch

You can run this script by registering mimetype with binfmt_misc because shebang already provided
'''

import os, sys
import argparse
from pathlib import Path
from dotenv import load_dotenv

dotenv_path = Path(__file__).parent / '.env'
load_dotenv(dotenv_path)

'''
Loading constants:
DEBUG
DB_NAME
DB_PASS
'''

DEBUG = os.environ.get("DEBUG")
DB_NAME = os.environ.get("DB_NAME") 
DB_PASS = os.environ.get("DB_PASS")

# Checking if the script is running as a subprocess
parent_pid = os.getppid() if hasattr(os, 'getppid') else None

def createParser (): # http://jenyay.net/Programming/Argparse
    parser = argparse.ArgumentParser(
                prog = sys.argv[0],
                description = '''Pyhton3 script bundle''',
                epilog = '''george.a.wise@gmail.com'''
                )
    parser.add_argument ('-v', '-verbose', nargs='?', const='1', default='0', help = 'Verbose output')
 
    return parser

def main(argv):
    parser = createParser()
    namespace = parser.parse_args()
    mode = namespace.v  # sys.argv[1]

    print(f"verbose mode: {mode}")
    

    sys.exit(os.EX_OK) # code 0, all ok

# assert __name__ is '__main__'
if __name__ == Path(__file__).stem:
	print('Usage error, this is not a module!')
	sys.exit(1)
if not sys.stdin.isatty() or not sys.stdout.isatty() or (parent_pid and parent_pid == None):
    print("Subprocess, no tty aviable!")
    sys.exit(1)
elif __name__ == '__main__':
    main(sys.argv)
else:
    sys.exit(os.EX_USAGE) # https://docs.python.org/2/library/os.html


