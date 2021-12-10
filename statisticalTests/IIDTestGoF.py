"""
Chi-Square Test (Goodness-of-fit, binary data)
REFERENCE: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90B.pdf (pg. 38 to 39)

Purpose: used to determine is data is independently and identically distributed (IID).
    Checks the distribution of ones in non-overlapping intervals of the human gameplay data
    to determine whether the distribution of ones remains the same throughout the sequence.

To run: IIDTestGoF.py data.txt
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

# INITIAL VALUES
print("INITIAL VALUES")
print("\tLet L be the number of values. L = %d." %L)
print("\tThere are", num0, "0s.")
print("\tThere are", num1, "1s.")

# Step 1
print("\nSTEP 1: Let p be the proportion of ones in the entire sequence S.")
p = num1/L

print("\tp = %f" %p)

# Step 2
print("\nSTEP 2: Partition S into ten non-overlapping subsets of length floor(L/10). If L is not a multiple of m, discard the remaining bits.")
Sd = []
sdString = ""
length = math.floor(L/10)
count = 0
for i in S:
    if (count == length):
        Sd.append(sdString)
        count = 0
        sdString = ""
    sdString = sdString + str(i)
    count = count+1

Sd.sort()
print("Sd =\n", Sd)
print("\tSize of Sd = %d.\n" %len(Sd))

# Step 3
print("\nSTEP 3: Initialize T to 0.")
T = 0
print("\tInitializing T = %d.\n" %T)

# Step 4
print("\nSTEP 4: Determine e0 and e1, the expected number of zeroes and ones, respectively.")
e0 = (1-p)*math.floor(L/10)
e1 = p*math.floor(L/10)

print("\tLet the expected number of zeros in each subsequence of Sd be %5f." %e0)
print("\tLet the expected number of ones in each subsequence of Sd be %5f.\n" %e1)

# Step 5
print("\nSTEP 5: For each subset in Sd, increment T with ((o0-e0)**2)/e0 + ((o1-e1)**2)/e1.")

for s in Sd:    # using the unique list
    o0 = 0      # num of 0s
    o1 = 0      # num of 1s
    for ss in s:
        if (ss == '0'):
            o0 = o0+1
        elif (ss == '1'):
            o1 = o1+1
    toAdd = ((o0-e0)**2)/e0 + ((o1-e1)**2)/e1
    T = T+toAdd
    print("\tFor %s...\to0 = %d\to1 = %d\t((o0-e0)**2)/e0 + ((o1-e1)**2)/e1 = %5f\n" %(s,o0,o1,toAdd))

# DETERMINING TEST SUCCESS
print("\nDETERMINING TEST SUCCESS")
degFreedom = 9  # hard-coded
crit = 27.887   # hard-coded

print("\tT = %.5f." %T)
print("\tdegrees of freedom = %d." %(degFreedom))
print("\tCritical value = %.3f." %(crit))

if (T > crit):
    print("\n\tThe test has failed. Therefore, the distribution of ones doesn't remain the same throughout the sequence.")
else:
    print("\n\tThe test has succeeded. Therefore, the distribution of ones remains the same throughout the sequence.")