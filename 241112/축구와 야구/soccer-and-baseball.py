n = int(input())

students = [tuple(map(int, input().split())) for _ in range(n)]
students.insert(0, (0, 0))  # 인덱스를 1부터 사용하기 위해 추가

dp = [[[-float('inf') for _ in range(12)] for _ in range(10)] for _ in range(n + 1)]
dp[0][0][0] = 0  # 초기 조건 설정

# i 명까지 보면서
# 야구팀에 j 명을
# 축구팀에 k 명을

for i in range(1, n + 1):
    s, b = students[i]
    for j in range(0, 10):
        for k in range(0, 12):
            if dp[i - 1][j][k] != -float('inf'):
                dp[i][j][k] = max(dp[i][j][k], dp[i - 1][j][k])

                if j + 1 <= 9:
                    dp[i][j + 1][k] = max(dp[i][j + 1][k], dp[i - 1][j][k] + b)

                if k + 1 <= 11:
                    dp[i][j][k + 1] = max(dp[i][j][k + 1], dp[i - 1][j][k] + s)

ans = dp[n][9][11]
print(ans)