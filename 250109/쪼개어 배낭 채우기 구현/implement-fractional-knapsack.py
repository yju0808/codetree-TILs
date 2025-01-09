


n, m = map(int, input().split())

goods = [tuple(map(int, input().split())) for _ in range(n)]


goods.sort(lambda x: -(x[1] / x[0]))

current = m
ans = 0

for w, v in goods:

    if w <= current:
        current -= w
        ans += v

    else:
        rest_w = current / w
        ans += v * rest_w
        break

print(f'{ans:.3f}')

