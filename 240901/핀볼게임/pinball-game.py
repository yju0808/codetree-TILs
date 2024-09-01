n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]


dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]


def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n



def simul(y, x, direction):

    time = 1
    visited = set()

    while is_valid_coord(y, x):

        visited.add((y, x, direction))

        if grid[y][x] == 1:
            
            if direction <= 1:
                direction = 1

            elif direction == 2:
                direction = 3

            elif direction == 3:
                direction = 2


        elif grid[y][x] == 2:
            if direction == 0:
                direction = 3

            elif direction == 1:
                direction = 2

            elif direction == 2:
                direction = 1

            elif direction == 3:
                direction = 0

        if (y + dy[direction], x + dx[direction], direction) in visited:
            return -1

        y += dy[direction]
        x += dx[direction]
        visited.add((y, x, direction))

        time += 1


    return time

ans = 0


for i in range(n):
    ans = max(ans, simul(i, 0, 0))
    ans = max(ans, simul(i, n - 1, 2))


for j in range(n):
    ans = max(ans, simul(0, j, 3))
    ans = max(ans, simul(n - 1, j, 1))


print(ans)