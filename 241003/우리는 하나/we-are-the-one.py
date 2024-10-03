from collections import deque

n, k, u, d = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]



cities = []
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

for i in range(n):
    for j in range(n):
        cities.append((i, j))


selected = []

ans = 0

def bfs(selected, visited):

    dq = deque()
    
    for y, x in selected:
        dq.append((y, x))
        visited[y][x] = True

    count = len(selected)

    while dq:

        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if is_valid_coord(ny, nx) and not visited[ny][nx] and u <= abs(grid[y][x] - grid[ny][nx]) <= d:
                dq.append((ny, nx))
                visited[ny][nx] = True
                count += 1

    return count


def select(last):

    global ans

    if len(selected) == k:
        visited = [[False for _ in range(n)] for _ in range(n)]
        ans = max(ans, bfs(selected, visited))
        return


    for i in range(last + 1, len(cities)):
        selected.append(cities[i])
        select(i)
        selected.pop()


select(-1)
print(ans)