

a = input()
b = input()

a = 'X' + a
b = 'X' + b

dp = [[0 for _ in range(len(b))] for _ in range(len(a))]

dp[1][1] = 0 if a[1] == b[1] else 1

for i in range(2, len(b)):
    if a[1] == b[i]:
        dp[1][i] = 1
    else:
        dp[1][i] = dp[1][i - 1] + 1

for i in range(2, len(a)):
    if a[i] == b[1]:
        dp[i][1] = 1
    else:
        dp[i][1] = dp[i - 1][1] + 1


for i in range(2, len(a)):
    for j in range(2, len(b)):

        if a[i] == b[j]:
            dp[i][j] = dp[i - 1][j - 1] 

        else:
            dp[i][j] = min(dp[i - 1][j - 1], dp[i - 1][j], dp[i][j - 1]) + 1


print(dp[len(a) - 1][len(b) - 1])