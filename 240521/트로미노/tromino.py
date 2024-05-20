block1 = ( 
    ((0, 0), (1, 0), (1, 1)), 
    ((0, 0), (0, 1), (1, 0)), 
    ((0, 0), (0, 1), (1, 1)),
    ((0, 1), (1, 1), (1, 0))
)

block2 = (
    ((0, 0), (0, 1), (0, 2)),
    ((0, 0), (1, 0), (2, 0))
)

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

def is_valid_coord(i, j):
    return 0 <= i < n and 0 <= j < m

ans = 0

for i in range(n):
    for j in range(m):

        for block in block1:

            is_placable = True
            num_sum = 0

            for x, y in block:
                if not is_valid_coord(i + x, j + y):
                    is_placable = False
                else:
                    num_sum += board[i + x][j + y]

            if is_placable:
                ans = max(ans, num_sum)

        for block in block2:
            
            is_placable = True
            num_sum = 0

            for x, y in block:
                if not is_valid_coord(i + x, j + y):
                    is_placable = False
                else:
                    num_sum += board[i + x][j + y]

            if is_placable:
                ans = max(ans, num_sum)

print(ans)