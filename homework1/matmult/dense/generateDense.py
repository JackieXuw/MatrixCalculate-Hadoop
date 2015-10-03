#!/usr/bin/env python

import sys
import random

# function to generate a single number
def randS():
	# generate a random float in this range [0, 5)
	return random.uniform(0, 5)

def main(argv):
	# judge if input is correct
	if len(sys.argv) != 4:
		print 'please enter three number (M, N, P) for creating dense matrix M * N & N * P'
		sys.exit()
	try:
		M = int(argv[0])
		N = int(argv[1])
		P = int(argv[2])
		print 'Input number is:', M, N, P
	except ValueError:
		print 'please enter three number (M, N, P) for creating dense matrix M * N & N * P'
		sys.exit()

	print 'Now generating matrices...'
	# start to generate the matrices
	# the output matrix is in this format:
	# matrix name + row number + value + value + ...
	# elements are delimitted by a single space
	
	# open the file and prepare to write to it
	matrices = open('matrices','w')
	# generate matrix A
	for row in xrange(0, M):
		line = 'A '
		line += str(row) + ' '
		for col in xrange(0, N):
			line += str(randS()) + ' '
		print line
		# now write this line to file
		line += '\n' # add line break
		matrices.write(line)

	# generate matrix B
	for row in xrange(0, N):
		line = 'B '
		line += str(row) + ' '
		for col in xrange(0, P):
			line += str(randS()) + ' '
		print line
		# now write this line to file
		line += '\n' # add line break
		matrices.write(line)

	print 'Done!'
	# close the file
	matrices.close()

if __name__ == "__main__":
    main(sys.argv[1:])
