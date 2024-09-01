from collections import deque

n, m, r, c = map(int, input().split())

dq = deque()

r -= 1
c -= 1

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


grid = [[0 for _ in range(n)] for _ in range(n)]


visited = set()
dq.append((r, c, 0))
grid[r][c] = 1

visited.add((r, c))


def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

while dq:
    
    y, x, time = dq.popleft()

    if time >= m:
        break

    dq.append((y, x, time + 1))

    for i in range(4):

        dist =  2 ** ((time + 1) - 1)

        ny = y + dy[i] * dist
        nx = x + dx[i] * dist

        if not (ny, nx) in visited and is_valid_coord(ny, nx):
            dq.append((ny, nx, time + 1))
            visited.add((ny, nx))
            grid[ny][nx] = 1
            

ans = 0

for i in range(n):
    for j in range(n):

        if grid[i][j]:
            ans += 1

print(ans)