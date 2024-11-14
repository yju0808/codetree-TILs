
n = int(input())

nums = [0 for _ in range(10)]

dp = [[0 for _ in range(10)] for _ in range(n + 1)]
MOD = 10 ** 9 + 7

for i in range(1, 10):
    dp[1][i] = 1


for i in range(2, n + 1):
    for j in range(10):
        for k in range(10):

            if i - 1 == k or k - 1 == i:
                
                dp[i][j] += (dp[i][k])
                dp[i][j] = dp[i][j] % MOD



ans = 0

for i in range(10):
    ans += dp[n][i]
    ans = ans % MOD

print(ans)