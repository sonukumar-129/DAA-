def stringConstruction(s):
    u = set(s)  
    return len(u)

import sys

input = sys.stdin.read
data = input().splitlines()

n = int(data[0])
r = []  
for i in range(1, n + 1):
    s = data[i]
    result = stringConstruction(s)
    r.append(result)


for res in r:
    print(res)
