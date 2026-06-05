#!/usr/bin/python3
# -*- coding: utf-8 -*-

"""
Script description: Empty python boilerplate skeleton wireframe template to start a new Python3 project from the scratch

You can run this script by registering mimetype with binfmt_misc because shebang already provided
"""

import argparse
import os
import signal
import sys
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path)

try:
    from dotenv import load_dotenv
except ImportError:
    print("This script requires the " + "\x1b[3m" + "dotenv" + "\x1b[0m" + " module.")
    print(
        "Caution: this script uses "
        + "\x1b[3m"
        + "--break-system-packages"
        + "\x1b[0m"
        + " key to install the module."
    )
    try:
        import pip

        print(f"pip {pip.__version__} has been found in your system.")
    except ImportError:
        print(
            "Pip is not installed in your system. We can't install "
            + "\033[1m"
            + "env_file"
            + "\033[0m"
            + " for you."
        )
        sys.exit(os.EX_NOHOST)
    ans = input("Do you want to install it? [y/N]: ").strip().lower()
    if (ans == "y" or ans != "") and ans != "n":
        os.system("pip install dotenv --break-system-packages")
        # TODO: pip install -r requirements.txt
        print("dotenv has been installed successfully. Please restart the script.")
        sys.exit(os.EX_OK)
    else:
        sys.exit(os.EX_NOHOST)

"""
Loading constants:
    VERSION
    DEBUG
    DB_NAME
    DB_PASS
"""
load_dotenv()  # Загружает переменные из файла .env

__version__ = os.environ.get("VERSION")
DEBUG = os.environ.get("DEBUG")
DB_NAME = os.environ.get("DB_NAME")
DB_PASS = os.environ.get("DB_PASS")

# Checking if the script is running as a subprocess
parent_pid = os.getppid() if hasattr(os, "getppid") else None


# Define the handler
def signal_handler(sig, frame):
    print("\nCtrl+C detected! Exiting...")
    sys.exit(0)


# Bind the signal to the handler
signal.signal(signal.SIGINT, signal_handler)


def createParser():  # http://jenyay.net/Programming/Argparse
    parser = argparse.ArgumentParser(
        prog=sys.argv[0],
        description="""Pyhton3 script bundle""",
        epilog="""george.a.wise@gmail.com""",
    )
    parser.add_argument(
        "-v", "-verbose", nargs="?", const="1", default="0", help="Verbose output"
    )

    return parser


def main(argv):
    parser = createParser()
    namespace = parser.parse_args()
    mode = namespace.v  # sys.argv[1]

    print(f"verbose mode: {mode}")
    print(f"version: {__version__}")

    sys.exit(os.EX_OK)  # code 0, all ok


# assert __name__ is '__main__'
if __name__ == Path(__file__).stem:
    print("Usage error, this is not a module!")
    sys.exit(1)
if (
    not sys.stdin.isatty()
    or not sys.stdout.isatty()
    or (parent_pid and parent_pid is None)
):
    print("Subprocess, no tty aviable!")
    sys.exit(1)
elif __name__ == "__main__":
    main(sys.argv)
else:
    sys.exit(os.EX_USAGE)  # https://docs.python.org/2/library/os.html
