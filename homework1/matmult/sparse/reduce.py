#!/usr/bin/env python
# in this mappper and reducer, I simply suppose M = 100, P = 100, N = 100
# hence A -> M * P -> 100 * 100, B -> P * N -> 100 * 100

# from operator import itemgetter
import sys

def main():
    # define the lastKeys to help detect the end of a certain block
    lastKeyI, lastKeyJ = None, None
    # define two dictionarys to store the needed value and identifier
    dictA = {}
    dictB = {}
    # input comes from STDIN
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # parse the input we got from map.py
        keyI, keyJ, matrix, identifier, val = line.split('\t')
        # debug use
        # print '%s\t%s\t%s\t%s\t%s' % (keyI, keyJ, matrix, identifier, val)

        #skip the first one
        if lastKeyI:
            # if the key pair changes, start calculate and output
            if keyI != lastKeyI or keyJ != lastKeyJ:
                # now calculate the current block's value
                currentVal = 0;
                for ident in dictA:
                    # check if the identifier is also in dictB
                    if ident in dictB:
                        currentVal += dictA[ident] * dictB[ident]
                # finish sum up, if sum isn't 0, then write it out
                if currentVal != 0:
                    print '%s %s %s' % (lastKeyI, lastKeyJ, currentVal)
                # key pair is changed, record it
                lastKeyI = keyI
                lastKeyJ = keyJ
                # clean up the dicts for new groups of values
                dictA = {}
                dictB = {}
            # store the first element of the new group
            if matrix == 'A':
                dictA[identifier] = int(val)
            else:
                dictB[identifier] = int(val)
        else: # store the key pair at the first time
            if matrix == 'A':
                dictA[identifier] = int(val)
            else:
                dictB[identifier] = int(val)                
            lastKeyI = keyI
            lastKeyJ = keyJ
    # if dicts is not empty, then there is still a group of value need to be calculated and printed out
    if dictA:
        # now calculate the current block's value
        currentVal = 0;
        for ident in dictA:
            # check if the identifier is also in dictB
            if ident in dictB:
                currentVal += dictA[ident] * dictB[ident]
        # finish sum up, if sum isn't 0, then write it out
        if currentVal != 0:
            print '%s %s %s' % (lastKeyI, lastKeyJ, currentVal)

if __name__ == "__main__":
    main()
