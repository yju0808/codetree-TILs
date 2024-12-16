

from sortedcontainers import SortedSet

s = SortedSet()

n, m = map(int, input().split())

nums = list(map(int, input().split()))

query = list(map(int, input().split()))

for n in nums:
    s.add(n)

for q in query:
    
    index = s.bisect_right(q)

    index -= 1

    if 0 <= index < len(s):
        print(s[index])
        s.remove(s[index])
        
    else:
        print(-1)