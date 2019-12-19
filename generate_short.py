# Create an array with all the alphanumeric

"""
ASCII CODE: 48 - 57
0 - 9

ASCII CODE: 65 - 90
A - Z

ASCII CODE: 97 - 122
a - z
"""

import random
arr = []
for i in range (9+1):
    arr.append(i)
for i in range (65,90+1):
    arr.append(chr(i))
for i in range (97,122+1):
    arr.append(chr(i))


print(random.choice(arr))
