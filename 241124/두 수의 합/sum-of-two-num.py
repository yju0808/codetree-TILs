

n, k = map(int, input().split())

nums = list(map(int, input().split()))
d = dict()

ans = 0

for n in nums:

    target = k - n

    if target in d:
        ans += d[target]

    if n in d:
        d[n] += 1
    else:
        d[n] = 1

print(ans)

