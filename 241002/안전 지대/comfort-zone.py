import sys

sys.setrecursionlimit(10000)


n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

max_k = 0

for i in range(n):
    for j in range(m):
        max_k = max(grid[i][j], max_k)


max_k -= 1


dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]




def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < m


def dfs(y, x, k):

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if is_valid_coord(ny, nx) and not visited[ny][nx] and grid[ny][nx] > k:
            visited[ny][nx] = True
            dfs(ny, nx, k)

ans = 1
max_safe_area_count = 0

for k in range(1, max_k + 1):

    visited = [[False for _ in range(m)] for _ in range(n)]

    safe_area_count = 0

    for i in range(n):
        for j in range(m):

            if not visited[i][j] and grid[i][j] > k:
                safe_area_count += 1
                dfs(i, j, k)

    
    if safe_area_count > max_safe_area_count:
        ans = k
        max_safe_area_count = safe_area_count


print(ans, max_safe_area_count)