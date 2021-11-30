"""
Runs Test
REFERENCE: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf (pg. 2-5 to 2-7)

Purpose: used to determine the randomness of a binary string.
    Looks at the total number of runs in the binary string, where a run is an uninterrupted sequence of bits.
    Tests whether the number of runs of ones and zeroes is as expected for a random sequence.
    Tests the "unpredictability" property.

To run: randomnessTestRuns.py random.txt
"""

import sys
import math
import collections

with open(sys.argv[1], 'r') as f:
    file = f.read()

epsilon = []      # S = data set
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
    epsilon.append(num)

n = len(epsilon)  # size of data set

# INITIAL VALUES
print("INITIAL VALUES")   
print("\tLet n be the number of values. n = %d." %n)
print("\tThere are", num0, "0s.")
print("\tThere are", num1, "1s.")

# Step 1
print("\nSTEP 1: Compute the pre-test proportion p of ones in the input sequence.")
p = num1/n
print("\tp =", p)

# Step 2
print("\nSTEP 2: Ensure that |p-1/2|<tau, in order to perform the test.")
tau = 2/math.sqrt(n)
result = abs(p-1/2)
print("\ttau = %f" %tau)
print("\t|p-1/2| = %f\n" %result)
if (result < tau):
    print("\tThe Runs test may be performed.")
else:
    print("\tThe Runs test need not be performed.\n")
    exit()

# Step 3
print("\nSTEP 3: Compute test statistics v_%d(obs).\nInitialize v_n(obs) = 1. Then for each bit in the string, if the next bit is the same the current bit, add 0 to v_n(obs). Otherwise, add 1." %n)
v_obs = 1
for i in range(n):
    if (i == (n-1)):
        break
    else:
        if (epsilon[i] == epsilon[i+1]):
            v_obs = v_obs + 0
        else:
            v_obs = v_obs + 1
print("\tv_%d(obs) = %d" %(n,v_obs))

# Step 4
print("\nSTEP 4: Compute p-value = erfc(|v_n(obs)-2*n*p*(1-p)|/(2*sqrt(2*n)*p*(1-p))).")
numerator = abs(v_obs-2*n*p*(1-p))
denominator = 2*math.sqrt(2*n)*p*(1-p)
pvalue = math.erfc((numerator)/(denominator))
print("\tp-value = %5f." %pvalue)

# DETERMINING TEST SUCCESS
print("\nDETERMINING TEST SUCCESS")
crit = 0.01
print("\tCritical value = %2f." %(crit))

if (pvalue < crit):
    print("\n\tAt the 1% confidence level, the test has failed. Therefore, the sequence is non-random.")
else:
    print("\n\tAt the 1% confidence level, the test has succeeded. Therefore, the sequence is random.")