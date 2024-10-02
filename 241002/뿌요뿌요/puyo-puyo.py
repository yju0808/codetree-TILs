n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]


dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


visited = [[False for _ in range(n)] for _ in range(n)]

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

def dfs(y, x, count):

    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        if is_valid_coord(ny, nx) and not visited[ny][nx] and grid[ny][nx] == grid[y][x]:
            visited[ny][nx] = True
            count = dfs(ny, nx, count + 1)

    
    return count


block_count = 0
max_block_size = 0


for i in range(n):
    for j in range(n):

        if is_valid_coord(i, j) and not visited[i][j]:

            visited[i][j] = True
            size = dfs(i, j, 1)

            if size >= 4:
                max_block_size = max(max_block_size, size)
                block_count += 1


print(block_count, max_block_size)