n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[-1 for _ in range(m)] for _ in range(n)]

dp[0][0] = 1

for i in range(1, n):
    for j in range(1, m):

        ans = -1

        for k in range(i):
            for l in range(j):

                if dp[k][l] == -1:
                    continue

                if grid[k][l] >= grid[i][j]:
                    continue

                ans = max(ans, dp[k][l] + 1)

        
        dp[i][j] = ans


print(max(map(max, dp)))