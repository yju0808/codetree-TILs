n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

dy = [
    [1, 2, -1, -2],
    [0, -1, 0, 1],
    [-1, -1, 1, 1]
]

dx = [
    [0, 0, 0, 0],
    [1, 0, -1, 0],
    [1, -1, 1, -1]
]


selected = []
points = []

for i in range(n):
    for j in range(n):
        if grid[i][j] == 1:
            points.append((i, j))

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

def cal_score():

    ans = set()

    for i in range(len(points)):

        y, x = points[i]
        bomb = selected[i]
        ans.add((y, x))


        for j in range(4):

            ny = y + dy[bomb][j]
            nx = x + dx[bomb][j]


            if is_valid_coord(ny, nx):
                ans.add((ny, nx))


    

    return len(ans)

result = 0

def select():

    global result

    if len(selected) == len(points):
        result = max(result, cal_score())
        return


    for i in range(3):
        selected.append(i)
        select()
        selected.pop()

select()
print(result)