n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]


nums = [i for i in range(n * n)]
selected = []
visited_i = [False for _ in range(n)]
visited_j = [False for _ in range(n)]

def cal_socre(selected):
    result = 0

    for row, col in selected:
        result += grid[row][col]

    return result

ans = -1


def solve(last_i, last_j):

    global ans

    if len(selected) == n:
        ans = max(ans, cal_socre(selected))
        return

    for i in range(n):
        for j in range(n):

            if visited_i[i] or visited_j[j]:
                continue
            
            selected.append((i, j))
            visited_i[i] = True
            visited_j[j] = True

            solve(i, j)

            selected.pop()
            visited_i[i] = False
            visited_j[j] = False



solve(-1, -1)
print(ans)