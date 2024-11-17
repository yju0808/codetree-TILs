

a = input()
b = input()

a = 'X' + a
b = 'X' + b

dp = [[0 for _ in range(len(b))] for _ in range(len(a))]

dp[0][0] = 0

for i in range(1, len(b)):
    dp[0][i] = i


for i in range(1, len(a)):
    dp[i][0] = i


for i in range(1, len(a)):
    for j in range(1, len(b)):

        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] 

        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1


print(dp[len(a) - 1][len(b) - 1])