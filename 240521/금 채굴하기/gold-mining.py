from collections import deque

n, m = map(int, input().split())

board = [list(map(int, input().split())) for _ in range(n)]

def get_cost(K):
    return K * K + (K + 1) * (K + 1)

elements = []

i = 0

while get_cost(i) <= n * n:

    dq = deque()

    dy = [-1, 0, 1, 0]
    dx = [0, 1, 0, -1]

    visited = set()

    dq.append((0, 0, 0))
    visited.add((0, 0))

    while True:

        c_y, c_x, turn = dq.popleft()

        if turn == i:
            break

        for j in range(4):

            n_y = c_y + dy[j] 
            n_x = c_x + dx[j]

            if (n_y, n_x) not in visited:
                visited.add((n_y, n_x))
                dq.append((n_y, n_x, turn + 1))

    elements.append(visited)
    i += 1


def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n

ans = 0


for i in range(n):
    for j in range(n):

        for element in elements:

            coin_count = 0
            for y, x in element:
                if is_valid_coord(i + y, j + x) and board[i + y][j + x] == 1:
                    coin_count += 1
                
            ans = max(ans, coin_count)

print(ans)