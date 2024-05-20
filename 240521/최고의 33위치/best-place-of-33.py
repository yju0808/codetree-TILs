N = int(input())

board = [list(map(int, input().split())) for _ in range(N)]

def is_valid_coord(i, j):
    return 0 <= i < N and 0 <= j < N

def get_coin_count(a, b):

    coin_count = 0

    for i in range(a, a + 3):
        for j in range(b, b + 3):
            coin_count += board[i][j]

    return coin_count

ans = 0

for i in range(N):
    for j in range(N):

        if (is_valid_coord(i + 2, j + 2)):
            ans = max(ans, get_coin_count(i, j))


print(ans)