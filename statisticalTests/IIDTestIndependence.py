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

# Step 2
print("\nFind the maximum integer m such that min(p0,p1)^m * floor(L/m) >= 5. If m > 11, let m = 11.")
m = 11
a = min(p0,p1)

while (m > 0):
    result = (a**m)*math.floor(L/m)
    print("m = %d...\tmin(p0,p1)^m * floor(L/m) = %5f" %(m, result))
    if (result < 5):
        m = m-1
    else:
        break
    
print("Thus, m = %d.\n" %(m))

# PART 2: Calculating T

# Step 1
T = 0
print("Initializing T = %d.\n" %T)

# Step 2
print("Partition S into non-overlapping m-bit blocks, denoted as B = (B_1, ... , B_(floor(L/m))). If L is not a multiple of m, discard the remaining bits.")
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
print("Size of B = %d.\n" %len(B))

dups = collections.Counter(B)   # find # of duplicates
dupsUnique = list(dups)         # list of unique duplicates

print("B, with only unique values =\n", dupsUnique)
print("Size of B (unique values only) = %d.\n" %len(dupsUnique))

# Step 3
print("For each possible m-bit tuple: determine o, w, e, to calculate (o-e)^2/e. Increment T by (o-e)^2/e.")

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
    print("For %s...\to = %d\tw = %d\te = %5f\t(o-e)^2/e = %5f\n" %(b,o,w,e,toAdd))

# DETERMINING TEST SUCCESS
crit = (2**m)-2

print("T = %5f." %T)
print("Critical value = %5f." %(crit))

if (T > crit):
    print("The test has failed. Therefore, the values are not independent.")
else:
    print("The test has succeeded. Therefore, the values are independent.")