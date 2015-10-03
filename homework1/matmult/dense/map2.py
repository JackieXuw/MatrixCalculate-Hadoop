#!/usr/bin/env python

import sys

def main():
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # directly emit the input
        print line

if __name__ == "__main__":
    main()
