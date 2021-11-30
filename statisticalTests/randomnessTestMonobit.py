"""
Frequency (Monobit) Test
REFERENCE: https://nvlpubs.nist.gov/nistpubs/Legacy/SP/nistspecialpublication800-22r1a.pdf (pg. 2-2 to 2-3)

Purpose: used to determine the randomness of a binary string.
    Tests the proportion of zeroes and ones for the entire sequence, determining  
    whether the proportions are approximately the same. 
    For a random string, the proportions should be about the same.
    Tests the "uniformity" property.

To run: randomnessTestMonobit.py random.txt
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

n = len(S)  # size of data set

# INITIAL VALUES
print("INITIAL VALUES")
print("\tLet n be the number of values. n = %d." %n)
print("\tThere are", num0, "0s.")
print("\tThere are", num1, "1s.")

# Step 1
print("\nSTEP 1: The zeros and ones are converted to values of –1 and +1, respectively, and are added together to produce Sn.")
Sn = num0*-1 + num1*1
print("\tSn =", Sn)

# Step 2
print("\nSTEP 2: Compute s_obs = |Sn|/sqrt(n).")
s_obs = abs(Sn)/math.sqrt(n)
print("\ts_obs = %f\n" %s_obs)

# Step 3
print("\nSTEP 3: Compute p-value = erfc(s_obs/sqrt(2)).")
p = math.erfc(s_obs/math.sqrt(2))
print("\tp = %5f." %p)

# DETERMINING TEST SUCCESS
print("\nDETERMINING TEST SUCCESS")
crit = 0.01
print("\tCritical value = %2f." %(crit))

if (p < crit):
    print("\n\tAt the 1% confidence level, the test has failed. Therefore, the sequence is non-random.")
else:
    print("\n\tAt the 1% confidence level, the test has succeeded. Therefore, the sequence is random.")