n, m = map(int, input().split())

jobs = [tuple(map(int, input().split())) for _ in range(n)]

max_e = 0

for e, t in jobs:
    max_e += e

dp = [float('inf') for _ in range(max_e + 1)]
dp[0] = 0

for e, t in jobs:
    for i in range(max_e, -1, -1):
        if i >= e:
            dp[i] = min(dp[i], dp[i - e] + t)

ans = float('inf')

for i in range(m, max_e + 1):
    ans = min(ans, dp[i])

if ans == float('inf'):
    ans = -1
print(ans)