
from sortedcontainers import SortedSet

s = SortedSet()

n, m = map(int, input().split())

for _ in range(n):
    s.add(tuple(map(int, input().split())))


for _ in range(m):

    q = tuple(map(int, input().split()))

    index = s.bisect(q)

    if index < len(s):
        print(*s[index])
    else:
        print(*(-1, -1))