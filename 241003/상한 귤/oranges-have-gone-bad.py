from collections import deque


n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

fruits = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 2:
            fruits.append((i, j))
            

dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]

ans = 0

def is_vaild_coord(y, x):
    return 0 <= y < n and 0 <= x < n



visited = [[False for _ in range(n)] for _ in range(n)]
dq = deque()

result = [[-2 for _ in range(n)] for _ in range(n)]

for i in range(n):
    for j in range(n):
        if grid[i][j] == 0:
            result[i][j] = -1

for y, x in fruits:
    dq.append((y, x, 0))
    visited[y][x] = True

while dq:

    y, x, time = dq.popleft()

    if grid[y][x] >= 1:
        result[y][x] = time

    for i in range(4):

        ny = y + dy[i]
        nx = x + dx[i]

        if is_vaild_coord(ny, nx) and not visited[ny][nx] and grid[ny][nx] != 0:
            visited[ny][nx] = True
            dq.append((ny , nx, time + 1))



for row in result:
    print(*row)