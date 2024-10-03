from collections import deque


n, h, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


def is_vaild_coord(y, x):
    return 0 <= y < n and 0 <= x < n

def bfs(y, x):

    visited = [[False for _ in range(n)] for _ in range(n)]
    dq = deque()
    dq.append((y, x, 0))
    visited[y][x] = True

    while dq:

        y, x, time = dq.popleft()

        if grid[y][x] == 3:
            return time


        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if is_vaild_coord(ny, nx) and not visited[ny][nx] and grid[ny][nx] != 1:
                visited[ny][nx] = True
                dq.append((ny , nx, time + 1))

    return -1

result = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            result[i][j] = bfs(i, j)


for row in result:
    print(*row)