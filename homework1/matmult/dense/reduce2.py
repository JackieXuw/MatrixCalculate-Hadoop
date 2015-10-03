#!/usr/bin/env python

import sys

def main():
	# initialize the sum
	result = 0
	lastRow, lastCol = None, None

	for line in sys.stdin:
	    # remove leading and trailing whitespace
	    line = line.strip()
	    # parse the input we got
	    row, col, val = line.split('\t')

	    # skip the first step
	    if lastRow:
	    	if lastRow != row or lastCol != col:
	    		# output the result
	    		print '%s\t%s\t%s' % (lastRow, lastCol, result)
	        	# reinitialize the sum and keys
	        	result = 0
	        	lastRow, lastCol = row, col
	        # add up value
	        result += float(val)
	    else:
	    	result += float(val)
	    	lastRow, lastCol = row, col

    # output the last tuple
	print '%s\t%s\t%s' % (lastRow, lastCol, result)

if __name__ == "__main__":
    main()
