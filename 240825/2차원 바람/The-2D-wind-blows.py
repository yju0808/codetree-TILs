n, m, q = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]





def rotate(r1, c1, r2, c2):


    temp = grid[r1][c2]
    for i in range(c2 - 1, c1, -1):
        grid[r1][i] = grid[r1][i - 1]

    temp2 = grid[r2][c2]
    for i in range(r2 - 1, r1, -1):
        grid[i][c2] = grid[i - 1][c2]
    
    grid[r1][c2] = temp


    temp = grid[r2][c1]
    for i in range(c1, c2 - 1):
        grid[r2][i] = grid[r2][i + 1]

    grid[r2][c2] = temp2

    for i in range(r1, r2 - 1):
        grid[i][c1] = grid[i + 1][c1]

    grid[r1][c1] = temp





for _ in range(q):

    r1, c1, r2, c2 = map(int, input().split())

    c1 -= 1
    c2 -= 1
    r1 -= 1
    r2 -= 1