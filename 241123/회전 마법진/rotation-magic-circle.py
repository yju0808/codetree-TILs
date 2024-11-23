
n = int(input())

current = input()
ideal =input()

current = ' ' + current
ideal = ' ' + ideal 

dp = [[float('inf') for _ in range(10)] for _ in range(n + 1)]

dp[0][0] = 0

for i in range(n):
    for j in range(10):

        cur = (int(current[i + 1]) + j) % 10
        ans = int(ideal[i + 1])

        cost = (ans - cur + 10) % 10
        nj = (j + cost) % 10
        dp[i + 1][nj] = min(dp[i + 1][nj], dp[i][j] + cost)

        cost = (cur - ans + 10) % 10
        nj = j
        dp[i + 1][nj] = min(dp[i + 1][nj], dp[i][j] + cost)


print(min(dp[n]))


