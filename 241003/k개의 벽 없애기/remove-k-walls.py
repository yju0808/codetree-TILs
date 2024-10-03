from collections import deque
n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

s_y, s_x = map(int, input().split())
e_y, e_x = map(int, input().split())

s_y -= 1
s_x -= 1
e_y -= 1
e_x -= 1


walls = []
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

for i in range(n):
    for j in range(n):
        if grid[i][j]:
            walls.append((i, j))


selected = []

ans = float('inf')

def bfs(y, x, visited):

    dq = deque()
    dq.append((y, x, 0))
    visited[y][x] = True

    while dq:

        y, x, time = dq.popleft()

        if y == e_y and x == e_x:
            return time

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if is_valid_coord(ny, nx) and not visited[ny][nx] and grid[ny][nx] != 1:
                dq.append((ny, nx, time + 1))
                visited[ny][nx] = True

    return -1


def select(last):

    global ans

    if len(selected) == k:

        visited = [[False for _ in range(n)] for _ in range(n)]

        for y, x in selected:
            grid[y][x] = 0
        
        result = bfs(s_y, s_x, visited)

        for y, x in selected:
            grid[y][x] = 1

        if result != -1:
            ans = min(ans, result)

    for i in range(last + 1, len(walls)):
        selected.append(walls[i])
        select(i)
        selected.pop()


select(-1)
print(ans if ans != float('inf') else - 1)