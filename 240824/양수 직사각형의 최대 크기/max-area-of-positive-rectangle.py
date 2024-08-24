n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]


def is_vaild_coord(y, x):
    return 0 <= y < n and 0 <= x < m


ans = -float('inf')


def get_score(y, x, h, w):

    result = 0

    for i in range(h):
        for j in range(w):

            if not is_vaild_coord(y + i, x + j) or grid[y + i][x + j] <= 0:
                return -1

    return h * w


ans = -1

for i in range(n):
    for j in range(m):
        for h in range(1, n + 1):
            for w in range(1, m + 1):

                result = get_score(i, j, h, w)

                if result > ans:
                    ans = result



print(ans)