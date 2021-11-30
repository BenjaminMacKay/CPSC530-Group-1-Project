"""
von Neumann extractor

Purpose: used to extract a random binary string from entropy.

To run: vonneumann.py data.txt
"""

import sys

def vonneumann(bs):
	if len(bs) > 1:
		bit1 = bs[0]
		bit2 = bs[1]
		if bit1 == bit2 and len(bs) != 2:
			return vonneumann(bs[2:])
		elif len(bs) != 2:
			return bit1+vonneumann(bs[2:])
		elif bit1 == bit2:
			return ''
		else:
			return bit1
	else:
		return ''

with open(sys.argv[1], 'r') as fr:
    file = fr.read()

S = []      # S = data set

for i in file:
    if (i == ' ' or i == '\n'):
        continue
    num = i
    S.append(num)

randomString =  vonneumann(S)

print('Random Stream:\n' + randomString)

with open("random.txt", 'w') as fw:
    fw.write(randomString)