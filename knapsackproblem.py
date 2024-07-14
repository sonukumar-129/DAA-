def u(n, c):
    r = []
    
    for case in c:
        s, t = case[0]
        e = case[1]
        
        dp = [0] * (t + 1)

        for v in e:
            for j in range(v, t + 1):
                dp[j] = max(dp[j], dp[j - v] + v)
        
        r.append(dp[t])
    
    return r

import sys

input = sys.stdin.read
data = input().splitlines()

k = int(data[0])
cases = []

line_index = 1
for _ in range(k):
    s, t = map(int, data[line_index].split())
    e = list(map(int, data[line_index + 1].split()))
    cases.append(((s, t), e))
    line_index += 2

results = u(k, cases)

for result in results:
    print(result)
