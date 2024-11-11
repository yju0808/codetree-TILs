n = int(input())

MOD = 10 ** 9 + 7

grades = ['G','B','T']

dp = [[[0 for _ in range(3)] for _ in range(3)] for _ in range(n +1)]
#i 문자열 길이
# j 총 받은 T의 개수 
# k 연속으로 B를 받은 개수


dp[1][0][0] = 1
dp[1][1][0] = 1
dp[1][0][1] = 1

for i in range(1, n + 1):
    for j in range(3):
        for k in range(3):

            count = dp[i - 1][j][k] 

            dp[i][j][0] += count
            dp[i][j][0] = dp[i][j][0] % MOD

            if j < 2:
                dp[i][j +1][0] += count
                dp[i][j +1][0] = dp[i][j + 1][0] % MOD
            
            if k < 2:
                dp[i][j][k + 1] += count
                dp[i][j][k + 1] = dp[i][j][k + 1] % MOD


ans = 0

for j in range(3):
    for k in range(3):
        ans += (dp[n][j][k] % MOD)

print(ans)