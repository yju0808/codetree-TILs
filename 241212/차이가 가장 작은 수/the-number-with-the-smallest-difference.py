
from sortedcontainers import SortedSet

s = SortedSet()

n, m = map(int, input().split())

nums = [int(input()) for _ in range(n)]

for i in nums:
    s.add(i)

ans = float('inf')

for i in nums:

    target = m + i

    index = s.bisect_right(target)

    if not (0 <= index < len(s)):
        continue

    ans = min(ans, abs(i - s[index]))

print(ans if ans != float('inf') else -1)


