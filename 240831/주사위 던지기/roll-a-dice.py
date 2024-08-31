n, m, r, c = map(int, input().split())

y = r - 1
x = c - 1

directions = input().split()

dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]

grid = [[0 for _ in range(n)] for _ in range(n)]

direction_mapper = {'L':2, 'R':0, 'U':1, 'D':3}

dice_mapper = [
    [4,2,3,5],
    [4,6,3,1],
    [2,6,5,1],
    [5,6,2,1],
    [3,6,4,1],
    [4,1,3,2]
]


up = 1
front = 2
right = 3

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


for direction in directions:

    grid[y][x] = 7 - up

    d = direction_mapper[direction]

    ny = y + dy[d]
    nx = x + dx[d]

    if not is_valid_coord(ny, nx):
        continue

    y = ny
    x = nx
    
    # ->
    if d == 0:
        up, front, right = 7 - right, front, up
    # ^
    elif d == 1:
        up, front, right = front, 7 - up, right

    # <-
    elif d == 2:
        up, front, right = right, front, 7 - up

    else:
        up, front, right = 7 - front, up, right



ans = 0

for i in range(n):
    for j in range(n):
        ans += grid[i][j]

print(ans)