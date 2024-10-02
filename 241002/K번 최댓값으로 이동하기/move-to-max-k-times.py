from collections import deque

n, k = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]

y, x = map(int, input().split())
y -= 1
x -= 1

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n



dq = deque()

visited = [[False for _ in range(n)] for _ in range(n)]
visited[y][x] = True

dq.append((y, x, 0))


def bfs(y, x):

    origin_num = grid[y][x]

    visited = [[False for _ in range(n)] for _ in range(n)]
    result = []

    dq = deque()
    dq.append((y, x))
    visited[y][x] = True

    while dq:

        y, x = dq.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if is_valid_coord(ny, nx) and not visited[ny][nx] and grid[ny][nx] < origin_num:
                dq.append((ny, nx))
                result.append((ny, nx))
                visited[ny][nx] = True
    
    return sorted(result)


cur_y = y 
cur_x = x


for i in range(k):
    
    result = bfs(cur_y, cur_x)

    cur_num = grid[cur_y][cur_x]
    temp_num = 0

    if not result:
        break

    for near_y, near_x in result:
        if cur_num > grid[near_y][near_x] and grid[near_y][near_x] > temp_num:
            temp_num = grid[near_y][near_x]
            cur_y = near_y 
            cur_x = near_x

    
print(cur_y + 1, cur_x + 1)