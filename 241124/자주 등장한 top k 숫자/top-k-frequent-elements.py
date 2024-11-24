
n, k = map(int, input().split())

nums = list(map(int, input().split()))
d = dict()

for n in nums:
    if n in d:
        d[n] += 1
    else:
        d[n] = 1

result = []
i = 0

for key, value in d.items():

    result.append((key, value))

    i+= 1
    if i == k:
        break

result.sort(lambda x: (-x[1], -x[0]))

for key, value in result:
    print(key, end= ' ')

