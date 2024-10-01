n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]


nums = [i for i in range(n * n)]
selected = []

visited_j = [False for _ in range(n)]

def cal_socre(selected):
    result = 0

    for row, col in selected:
        result += grid[row][col]

    return result

ans = -1


def solve(last_i):

    global ans

    if len(selected) == n:
        ans = max(ans, cal_socre(selected))
        return

    for i in range(last_i + 1, n):
        for j in range(n):

            if visited_j[j]:
                continue
            
            selected.append((i, j))
            visited_j[j] = True

            solve(i)

            selected.pop()
            visited_j[j] = False



solve(-1)
print(ans)