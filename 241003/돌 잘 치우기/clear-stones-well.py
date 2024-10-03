from collections import deque
n, k, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

starts = [list(map(int, input().split())) for _ in range(k)]
rocks = []

for i in range(len(starts)):
    y, x = starts[i]
    starts[i] = (y - 1, x - 1)

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

for i in range(n):
    for j in range(n):
        if grid[i][j]:
            rocks.append((i, j))


selected = []

ans = 0

def bfs(y, x, visited):

    dq = deque()
    dq.append((y, x))
    visited[y][x] = True
    count = 1

    while dq:

        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if is_valid_coord(ny, nx) and not visited[ny][nx] and grid[ny][nx] != 1:
                dq.append((ny, nx))
                visited[ny][nx] = True
                count += 1

    return count


def select(last):

    global ans

    if len(selected) == m:

        result = 0
        visited = [[False for _ in range(n)] for _ in range(n)]

        for y, x in selected:
            grid[y][x] = 0
        
        for y, x in starts:

            if not visited[y][x]:
                temp = bfs(y, x, visited)
                result += temp

        for y, x in selected:
            grid[y][x] = 1

        ans = max(ans, result)


    for i in range(last + 1, len(rocks)):
        selected.append(rocks[i])
        select(i)
        selected.pop()




select(-1)
print(ans)