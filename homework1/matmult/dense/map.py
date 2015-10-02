#!/usr/bin/env python
# in this mappper and reducer, a precondition is that the matrices are square

import sys

def main():
    # define the calculation maximum block size -> B * B
    B = 2
    # input comes from STDIN (standard input)
    for line in sys.stdin:
        # remove leading and trailing whitespace
        line = line.strip()
        # split the line into elements
        elements = line.split(' ')
        # get the matrix name
        matrix = elements[0]
        # get the size of matrix
        N = int(elements[1])
        # get the current row
        row = int(elements[2])

        # consider the N could be super large, and might not be able to fit in memory, so we emit this block by block
        # calculate current Block in row aspect
        currentBlockRow = row / B
        # calculate the needed blocks
        if N % B == 0:
            maxBlock = N / B
        else:
            maxBlock = N / B + 1

        currentBlockCol = 0;
        while currentBlockCol < maxBlock:
            # calculate current position
            curPos = currentBlockCol * B

            # now create the key and value pair
            blockKey = str(currentBlockRow) + '\t'
            blockKey += str(currentBlockCol) + '\t'
            tuples = matrix

            # start retrieving current block
            i = 0
            while curPos + i < N and i < B:
                tuples += '\t' + str(elements[3 + curPos + i])
                i += 1
            # emit the whole message
            print (blockKey + tuples)
            currentBlockCol += 1

if __name__ == "__main__":
    main()
