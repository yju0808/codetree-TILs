


n, m = map(int, input().split())

nums = list(map(int, input().split()))
queries = list(map(int, input().split()))
d = {}
for n in nums:
    
    if n in d:
        d[n] += 1
    else:
        d[n] = 1


for q in queries:

    if q not in d:
        print(0, end = ' ')
    else:
        print(d[q], end=' ')