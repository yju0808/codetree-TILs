import math

n, m = map(int, input().split())

points = [list(map(int, input().split())) for _ in range(n)]
selected = []


def cal_dist(p1, p2):
    x1, y1 = p1
    x2, y2 = p2

    return math.sqrt(((x1 - x2) ** 2 + (y1 - y2) ** 2))

ans = float('inf')


def cal_ans(selected):

    result = 0

    for i in range(len(selected)):
        for j in range(len(selected)):

            if i == j:
                continue

            result = max(result, cal_dist(selected[i], selected[j]))


    return result


def solve(last):

    global ans

    if len(selected) == m:
        ans = min(ans, cal_ans(selected))
        return

    for i in range(last + 1, len(points)):
        selected.append(points[i])
        solve(i)
        selected.pop()


solve(-1)

print(int(ans ** 2))