n = int(input())

jobs = [tuple(map(int, input().split())) for _ in range(n)]

jobs.sort(lambda x: x[1])

dp = [0 for _ in range(n)]

dp[0] = jobs[0][2]

for i in range(1, n):
    for j in range(i):

        if jobs[i][0] > jobs[j][1]:
            dp[i] = max(dp[i], dp[j] + jobs[j][2])

print(max(dp))