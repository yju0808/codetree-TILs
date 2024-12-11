
from sortedcontainers import SortedSet

s = SortedSet()


n, m = map(int, input().split())

nums = list(map(int, input().split()))

for i in range(1, m +1):
    s.add(-i)

count = 0

for i in nums:
    
    index = s.bisect_left(-i)

    if 0 <= index < len(s):
        s.remove(s[index])
        count += 1
    else:
        break

print(count)

