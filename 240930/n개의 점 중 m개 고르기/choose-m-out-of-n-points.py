import math

n, m = map(int, input().split())

points = [list(map(int, input().split())) for _ in range(n)]
selected = []


def cal_dist(p1, p2):
    y1, x1 = p1
    y2, x2 = p2

    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

ans = float('inf')

def solve(last):

    global ans

    if len(selected) == 2:
        ans = min(ans, cal_dist(selected[0], selected[1]))
        return

    for i in range(last + 1, len(points)):
        selected.append(points[i])
        solve(i)
        selected.pop()


solve(-1)

print(int(ans ** 2))