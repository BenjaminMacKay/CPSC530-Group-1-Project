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

# Step 1
print("\nLet p be the proportion of ones in the entire sequence S.")
p = num1/L

print("p = %f\n" %p)

# Step 2
print("Partition S into ten non-overlapping subsets of length floor(L/10). If L is not a multiple of m, discard the remaining bits.")
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
print("Size of Sd = %d.\n" %len(Sd))

# Step 3
T = 0
print("Initializing T = %d.\n" %T)

# Step 4
e0 = (1-p)*math.floor(L/10)
e1 = p*math.floor(L/10)

print("Let the expected number of zeros in each subsequence of Sd be %5f.\n" %e0)
print("Let the expected number of ones in each subsequence of Sd be %5f.\n" %e1)

# Step 3
print("For each subset in Sd...")

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
    print("For %s...\to0 = %d\to1 = %d\t((o0-e0)**2)/e0 + ((o1-e1)**2)/e1 = %5f\n" %(s,o0,o1,toAdd))

# DETERMINING TEST SUCCESS
crit = 27.887

print("T = %5f." %T)
print("Critical value = %5f." %(crit))

if (T > crit):
    print("The test has failed. Therefore, the distribution of ones doesn't remain the same throughout the sequence.")
else:
    print("The test has succeeded. Therefore, the distribution of ones remains the same throughout the sequence.")