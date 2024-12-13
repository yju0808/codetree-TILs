from sortedcontainers import SortedSet

s = SortedSet()      

n, m = map(int, input().split())

for _ in range(n):
    s.add(tuple(map(int, input().split())))


for _ in range(m):

    k = int(input())

    index = s.bisect_left((k, 0))

    if 0 <= index < len(s):
        print(*s[index])
        s.remove(s[index])
        
    else:
        print(*(-1, -1))
