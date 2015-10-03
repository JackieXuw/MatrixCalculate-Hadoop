#!/usr/bin/env python

import sys

def main():
    # define the calculation maximum block size and matrix size:
    # m * n for A, origin M * N
    # n * p for B, origin N * P
    m, n, p = 2, 2, 2
    M, N, P = 4, 4, 4

    # define the lastKeys to help detect the end of a certain block
    lastKeyI, lastKeyJ, lastKeyK = None, None, None

    # define some containers to store the values and result
    listA = []
    listB = []
    resultMap = {}
    # initialize the result map with 0
    for i in xrange(0, m):
        for j in xrange(0, p):
            hashKey = str(i) + ',' + str(j)
            resultMap[hashKey] = 0

    # input comes from STDIN
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # parse the input we got from map.py
        elements = line.split('\t')
        keyI, keyJ, keyK = elements[0], elements[1], elements[2]
        identifierRow, identifierCol = elements[3], elements[4]
        matrix, value = elements[5], float(elements[6])
        
        # debug use
        # print '%s\t%s\t%s\t%s\t%s\t%s\t%s' % (keyI, keyJ, keyK, identifierRow, identifierCol, matrix, value)

        #skip the first one
        if lastKeyI:
            # if the key pair changes, start calculate and output
            if keyI != lastKeyI or keyJ != lastKeyJ or keyK != lastKeyK:
                # loop over two list to seek anything needed to be multiplied
                for tupleA in listA:
                    for tupleB in listB:
                        # if A.identifierCol == B.identifierCol
                        if tupleA[1] == tupleB[0]:
                            hashKey = tupleA[0] + ',' + tupleB[1]
                            resultMap[hashKey] += tupleA[2] * tupleB[2]
                # finished current section, now print it
                for i in xrange(0, m):
                    for j in xrange(0, p):
                        # do not overflow
                        if int(lastKeyI) * m + i < M and int(lastKeyK) * p + j < P:
                            hashKey = str(i) + ',' + str(j)
                            # convert the block position back to matrix position
                            print '%s\t%s\t%s' % (int(lastKeyI) * m + i, int(lastKeyK) * p + j, resultMap[hashKey])
                # reinitialize the containers
                listA = []
                listB = []
                resultMap = {}
                for i in xrange(0, m):
                    for j in xrange(0, p):
                        hashKey = str(i) + ',' + str(j)
                        resultMap[hashKey] = 0
                # set last keys
                lastKeyI = keyI
                lastKeyJ = keyJ
                lastKeyK = keyK                
            # store the value
            if matrix == 'A':
                listA.append([identifierRow, identifierCol, value])
            elif matrix == 'B':
                listB.append([identifierRow, identifierCol, value])

        else:
            # store the value
            if matrix == 'A':
                listA.append([identifierRow, identifierCol, value])
            elif matrix == 'B':
                listB.append([identifierRow, identifierCol, value])
            lastKeyI = keyI
            lastKeyJ = keyJ
            lastKeyK = keyK

    # there should be still one block needed to be emitted
    if listA:
        # loop over two list to seek anything needed to be multiplied
        for tupleA in listA:
            for tupleB in listB:
                # if A.identifierCol == B.identifierCol
                if tupleA[1] == tupleB[0]:
                    hashKey = tupleA[0] + ',' + tupleB[1]
                    resultMap[hashKey] += tupleA[2] * tupleB[2]
        # finished current section, now print it
        for i in xrange(0, m):
            for j in xrange(0, p):
                # do not overflow
                if int(lastKeyI) * m + i < M and int(lastKeyK) * p + j < P:
                    hashKey = str(i) + ',' + str(j)
                    # convert the block position back to matrix position
                    print '%s\t%s\t%s' % (int(lastKeyI) * m + i, int(lastKeyK) * p + j, resultMap[hashKey])

if __name__ == "__main__":
    main()
