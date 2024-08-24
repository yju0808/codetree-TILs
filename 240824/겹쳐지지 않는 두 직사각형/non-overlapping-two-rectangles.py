n, m = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]


def is_vaild_coord(y, x):
    return 0 <= y < n and 0 <= x < m

def get_score(y, x , h, w, checked, is_two):

    result = 0

    for i in range(h):
        for j in range(w):

            if not is_vaild_coord(y + i, x + j) or (y + i, x + j) in checked:
                return -float('inf')

            result += grid[y + i][x + j]

            if not is_two:
                checked.add((y + i, x + j))
        
    return result


ans = -float('inf')

for i in range(n):
    for j in range(m):
        for h in range(1, n + 1):
            for w in range(1, m + 1):

                result = 0
                checked = set()
                
                result += get_score(i, j, h, w, checked, False)

                for i2 in range(n):
                    for j2 in range(m):
                        for h2 in range(1, n + 1):
                            for w2 in range(1, m + 1):

                                ans = max(result + get_score(i2, j2, h2, w2, checked, True), ans)

                
print(ans)