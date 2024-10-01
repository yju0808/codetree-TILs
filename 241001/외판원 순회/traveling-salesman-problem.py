n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

visitied = [False for _ in range(n)]

selected = [0]

def cal_dist(selected):

    result = 0

    for i in range(0, len(selected) - 1):
        cur = selected[i]
        ne = selected[i + 1]

        if not grid[cur][ne]:
            return float('inf')

        result += grid[cur][ne]

    if not grid[selected[-1]][0]:
        return float('inf')
        
    result += grid[selected[-1]][0]
    return result

ans = float('inf')


def solve():
    global ans

    if len(selected) == n:
        ans = min(ans, cal_dist(selected))
        return

    for i in range(1, n):
        if visitied[i]:
            continue

        selected.append(i)
        visitied[i] = True

        solve()

        selected.pop()
        visitied[i] = False


solve()
print(ans)