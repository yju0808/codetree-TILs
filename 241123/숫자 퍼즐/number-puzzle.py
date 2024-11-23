
n, m, k_ = map(int, input().split())

dp = [[[0 for _ in range(201)] for _ in range(201)] for _ in range(n + 1)]

for i in range(1, m + 1):
    dp[1][i][i] = 1

for i in range(1, n):
    for j in range(1, m + 1):
        for k in range(1, m + 1):
            for l in range(1, k + 1):

                if j + l > m:
                    break

                dp[i + 1][j + l][l] += dp[i][j][k]


cur_l = 1
cur_m = m

for i in range(n, 0, -1):
        while dp[i][cur_m][cur_l] < k_:
            k_ -= dp[i][cur_m][cur_l]
            cur_l += 1

        print(cur_l, end = ' ')
        cur_m -= cur_l
    