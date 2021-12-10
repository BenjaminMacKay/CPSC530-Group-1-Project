"""
Chi-Square Test (Independence, binary data)
REFERENCE: https://nvlpubs.nist.gov/nistpubs/SpecialPublications/NIST.SP.800-90B.pdf (pg. 37 to 38)

Purpose: used to determine is data is independently and identically distributed (IID).
    Checks the independence assumption of binary data, ensuring the data gathered from human gameplay is independent.
    Note use of m-bit tuples rather than between single adjacent bits.

To run: IIDTestIndependence.py data.txt
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
print("Let L be the number of values. L = %d." %L)
print("There are", num0, "0s.")
print("There are", num1, "1s.")

# PART 1: DETERMINING m
print("\nPART 1: DETERMINING m\n")

# Step 1
print("\nSTEP 1.1: Let p0 and p1 be the proportion of zeroes and ones in S, respectively.")
p0 = num0/L
p1 = num1/L

print("\tp0 =", p0)
print("\tp1 =", p1)

# Step 2
print("\nSTEP 1.2: Find the maximum integer m such that min(p0,p1)^m * floor(L/m) >= 5. If m > 11, let m = 11.")
m = 11
a = min(p0,p1)

while (m > 0):
    result = (a**m)*math.floor(L/m)
    print("\tm = %d...\tmin(p0,p1)^m * floor(L/m) = %5f" %(m, result))
    if (result < 5):
        m = m-1
    else:
        break
    
print("\tThus, m = %d.\n" %(m))

# PART 2: Calculating T
print("PART 2: CALCULATING T\n")

# Step 1
print("\nSTEP 2.1: Initialize T to 0.")
T = 0
print("\tInitializing T = %d." %T)

# Step 2
print("\nSTEP 2.2: Partition S into non-overlapping m-bit blocks, denoted as B = (B_1, ... , B_(floor(L/m))). If L is not a multiple of m, discard the remaining bits.")
B = []
bString = ""
count = 0
for i in S:
    if (count == 5):
        B.append(bString)
        count = 0
        bString = ""
    bString = bString + str(i)
    count = count+1

B.sort()
print("B =\n", B)
print("\tSize of B = %d.\n" %len(B))

dups = collections.Counter(B)   # find # of duplicates
dupsUnique = list(dups)         # list of unique duplicates

print("B, with only unique values =\n", dupsUnique)
print("\tSize of B (unique values only) = %d." %len(dupsUnique))

# Step 3
print("\nSTEP 2.3: For each possible m-bit tuple: determine o, w, e, to calculate (o-e)^2/e. Increment T by (o-e)^2/e.")

#for b in B:            # using the not unique list
for b in dupsUnique:    # using the unique list
    o = dups[b]
    w = 0
    for c in b:
        if (c == '1'):
            w = w+1
    e = (p1**w)*(p0**(m-w))*(math.floor(L/m))
    toAdd = ((o-e)**2)/e
    T = T+toAdd
    print("\tFor %s...\to = %d\tw = %d\te = %5f\t(o-e)^2/e = %5f\n" %(b,o,w,e,toAdd))

# DETERMINING TEST SUCCESS
print("\nDETERMINING TEST SUCCESS")
degFreedom = (2**m)-2
crit = 59.703   # hard-coded

print("\tT = %.5f." %T)
print("\tdegrees of freedom = %d." %(degFreedom))
print("\tCritical value (type I error is 0.001) = %.3f." %crit)

if (T > crit):
    print("\n\tThe test has failed. Therefore, the values are not independent.")
else:
    print("\n\tThe test has succeeded. Therefore, the values are independent.")