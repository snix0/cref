#!/usr/bin/env python3
import importlib.resources as pkg_resources
#from . import templates
import templates
import sys
from colorama import Fore
from colorama import Style
import colorama


def refLookup(ref):
    template = pkg_resources.read_text(templates, ref)
    res = ""
    for line in template.split('\n'):
        res += (Fore.BLUE + line if line.startswith("#") else Fore.YELLOW + line) + "\n"
    return res

def printUsage():
    print("Usage: %s [ARG]" % sys.argv[0])

if __name__ == '__main__':
    colorama.init()

    if len(sys.argv) < 2:
        printUsage()
        sys.exit(1)
    else:
        print("Fetching quick reference for: " + Fore.GREEN + sys.argv[1] + "\n")
        print(Fore.BLUE +  refLookup(sys.argv[1]) + Style.RESET_ALL)
