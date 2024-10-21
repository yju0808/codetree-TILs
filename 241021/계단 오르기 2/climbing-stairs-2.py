# 계단의 층 수를 입력받습니다.
n = int(input())
coin = [0] * (n + 1)


coin =  list(map(int, input().split()))
coin.insert(0, 0)

dp = [[0 for _ in range(4)] for _ in range(n + 1)]


dp[1][1] = coin[1]
if n > 1:
    dp[2][0] = coin[2]
    dp[2][2] = coin[1] + coin[2]


for i in range(3, n + 1):
    for j in range(4):
        if dp[i-2][j] != 0:
            dp[i][j] = max(dp[i][j], dp[i - 2][j] + coin[i])
        if j and dp[i - 1][j - 1] != 0:
            dp[i][j] = max(dp[i][j], dp[i - 1][j - 1] + coin[i])


ans = max(dp[n])
print(ans)