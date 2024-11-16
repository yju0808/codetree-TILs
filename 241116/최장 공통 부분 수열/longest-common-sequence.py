

a = input()
b = input()

dp = [[0 for _ in range(len(b) + 1)] for _ in range(len(a) +1)]
dp[0][0] = 1 if a[0] == b[0] else 2

for i in range(len(a)):
    for j in range(len(b)):

        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] + 1

        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])


ans = dp[len(a) - 1][len(b) - 1]

print(ans)