n = int(input())

y, x = map(int, input().split())

grid = [input() for _ in range(n)]


dy = [0, 1, 0, -1]
dx = [1, 0, -1, 0]


direction = 0
time = 0

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

ny = y
nx = x

ans = -1
visited = set()


while True:

    if (ny, nx, direction) in visited:
        break
    
    if not is_valid_coord(ny + dy[direction], nx + dx[direction]):
        ans = time
        break

    ny += dy[direction]
    nx += dx[direction]

    visited.add((ny, nx, direction))

    time += 1

    if grid[ny][nx] == '#':
        visited.remove((ny, nx, direction))
        ny -= dy[direction]
        nx -= dx[direction]
        direction = (direction + 1) % 4
        time -= 1
        continue


    right_direction = direction + 1
        
    right_y = ny + dy[right_direction]
    right_x = nx + dx[right_direction]

    if is_valid_coord(right_y, right_x) and grid[right_y][right_x] == '#':
        ny += dy[direction]
        nx += dx[direction]

        visited.add((ny, nx, direction))
        time += 1

    else:
        direction = direction - 1 if direction - 1 >= 0 else 3
        ny += dy[direction]
        nx += dx[direction]

        visited.add((ny, nx, direction))
        time += 1