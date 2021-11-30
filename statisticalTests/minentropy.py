"""
min-entropy extractor

Purpose: used to calculate min-entropy.

To run: minentropy.py data.txt
"""

import sys
import math
import collections

with open(sys.argv[1], 'r') as f:
    file = f.read()

S = []      # S = data set
num0 = 0    # number of 0s
num1 = 0    # number of 1s

for i in file:
    if (i == ' ' or i == '\n'):
        continue
    num = int(i)
    if (num == 0):
        num0 = num0 + 1
    elif (num == 1):
        num1 = num1 + 1
    S.append(num)

L = len(S)  # size of data set

print("Let L be the number of values. L = %d." %L)
print("There are", num0, "0s.")
print("There are", num1, "1s.")

# PART 1: DETERMINING m

# Step 1
print("\nLet p0 and p1 be the proportion of zeroes and ones in S, respectively.")
p0 = num0/L
p1 = num1/L

print("p0 =", p0)
print("p1 =", p1)

minEntropy = -1*math.log(max(p0,p1),2)

print("\nThe min entropy is %f.\n" %minEntropy)