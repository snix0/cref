#!/usr/bin/env python3
import importlib.resources as pkg_resources
#from . import templates
import templates
import sys


def refLookup(ref):
    template = pkg_resources.read_text(templates, ref)
    return template

def printUsage():
    print("Usage: %s [ARG]" % sys.argv[0])

if __name__ == '__main__':
    if len(sys.argv) < 2:
        printUsage()
        sys.exit(1)
    else:
        print(refLookup(sys.argv[1]))
