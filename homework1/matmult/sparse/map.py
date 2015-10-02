#!/usr/bin/env python
# in this mappper and reducer, I simply suppose M = 100, P = 100, N = 100
# hence A -> M * P -> 100 * 100, B -> P * N -> 100 * 100

import sys

def main():
    M, N = 100, 100
    # M, N = 4, 4
    # M, N = 2, 3
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into elements
        matrix, row, column, val = line.split(' ')
        if matrix == 'A':
            for i in xrange(0, N):
                # first two elements represent the key pair, after are the needed messages, like this {(i, k), (A or B, j, value)}, k in 0 to N - 1
                print '%s\t%s\t%s\t%s\t%s' % (row, i, matrix, column, val)
        elif matrix == 'B':
            for i in xrange(0, M):
                # first two elements represent the key pair, after are the needed messages, like this {(k, j), (A or B, i, value)}, k in 0 to M - 1
                print '%s\t%s\t%s\t%s\t%s' % (i, column, matrix, row, val)

if __name__ == "__main__":
    main()
