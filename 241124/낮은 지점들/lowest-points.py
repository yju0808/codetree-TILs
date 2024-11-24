
n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]

d = dict()

for x, y in points:

    if x in d:
        if d[x] > y:
            d[x] = y

    else:
        d[x] = y


ans = 0

for x, y in d.items():
    ans += y

print(ans)