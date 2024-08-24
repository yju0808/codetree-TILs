n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]


def is_vaild_coord(y, x):
    return 0 <= y < n and 0 <= x < m

def get_score(y, x , h, w, checked):

    result = 0

    for i in range(h):
        for j in range(w):

            if not is_vaild_coord(y + i, x + j) or checked[y + i][x + j]:
                return -float('inf')

            result += grid[y + i][x + j]
            checked[y + i][x + j] = True


    return result


ans = -float('inf')

for i in range(n):
    for j in range(m):
        for h in range(1, n):
            for w in range(1, m):

                result = 0
                checked = [[False for _ in range(m)] for _ in range(n)]
                
                result += get_score(i, j, h, w, checked)

                for i2 in range(n):
                    for j2 in range(m):
                        for h2 in range(1, n):
                            for w2 in range(1, m):

                                result += get_score(i2, j2, h2, w2, checked)
                                ans = max(result, ans)

                
print(ans)