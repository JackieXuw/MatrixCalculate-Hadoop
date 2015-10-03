#!/usr/bin/env python

import sys

def main():
    # define the calculation maximum block size and matrix size:
    # m * n for A, origin M * N
    # n * p for B, origin N * P
    m, n, p = 2, 2, 2
    M, N, P = 4, 4, 4

    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into elements
        elements = line.split(' ')
        # get the total column number of this line
        totalCol = len(elements) - 2
        # get the matrix name
        matrix = elements[0]
        # get the current row
        curRow = int(elements[1])

        # consider the matrix size could be super large, and might not be able to fit in memory, so we do the calculatation block by block
        if matrix == 'A':
            if P % p == 0:
                emitNumber = P / p
            else:
                emitNumber = P / p + 1
            blockRow = m
            blockCol = n
        elif matrix == 'B':
            if M % m == 0:
                emitNumber = M / m
            else:
                emitNumber = M / m + 1
            blockRow = n
            blockCol = p
        # calculate current Block in row aspect
        currentBlockRow = curRow / blockRow
        # calculate the needed blocks in column aspect
        if totalCol % blockCol == 0:
            blocksInCol = totalCol / blockCol
        else:
            blocksInCol = totalCol / blockCol + 1

        currentBlockCol = 0;
        while currentBlockCol < blocksInCol:
            # calculate current column position
            curColPos = currentBlockCol * blockCol

            # now create the key and value pair
            blockKey = str(currentBlockRow) + '\t'
            blockKey += str(currentBlockCol) + '\t'
            tuples = str(curRow % blockRow) + '\t'

            # start retrieving current block
            i = 0
            while curColPos + i < totalCol and i < blockCol:
                # emit the whole message in this format:
                # (blockkey -> three values), (matrix name, row position in block, column position in block, value)
                if matrix == 'A':
                    for j in xrange(0, emitNumber):
                        print (blockKey + str(j) + '\t' + tuples + str(i) + '\t' + matrix + '\t' + str(elements[2 + curColPos + i]))
                elif matrix == 'B':
                    for j in xrange(0, emitNumber):
                        print (str(j) + '\t' + blockKey + tuples + str(i) + '\t' + matrix + '\t' + str(elements[2 + curColPos + i]))
                i += 1

            # increase current block number in column, continue looping
            currentBlockCol += 1

if __name__ == "__main__":
    main()
