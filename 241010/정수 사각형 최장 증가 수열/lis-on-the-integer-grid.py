n = int(input())

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

grid = [list(map(int, input().split())) for _ in range(n)]

dp = [[1 for _ in range(n)] for _ in range(n)]


nums = []

for i in range(n):
    for j in range(n):
        nums.append((grid[i][j], i, j))

nums.sort()

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


for _, y, x in nums:

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if is_valid_coord(ny, nx) and grid[ny][nx] > grid[y][x]:
            dp[ny][nx] = max(dp[ny][nx], dp[y][x] + 1)



ans = 0

for i in range(n):
    for j in range(n):
        ans = max(ans, dp[i][j])

print(ans)