n = int(input())

cards1 = list(map(int, input().split()))
cards2 = list(map(int, input().split()))

cards1.insert(0, 0)
cards2.insert(0, 0)

dp = [[-1 for _ in range(n + 1)] for _ in range(n + 1)]
dp[0][0] = 0

for i in  range(n):
    for j in range(n):

        if dp[i][j] == -1:
            continue

        if cards1[i + 1] < cards2[j +1]:
            dp[i +1][j] = max(dp[i + 1][j], dp[i][j])


        if cards1[i + 1] > cards2[j + 1]:
            dp[i][j + 1] = max(dp[i][j + 1], dp[i][j] + cards2[j + 1])

        dp[i + 1][j + 1] = max(dp[i + 1][j +1], dp[i][j])


ans = 0


for i in range(n +1):
    ans = max(ans, dp[i][n])
    ans = max(ans, dp[n][i])

print(ans)