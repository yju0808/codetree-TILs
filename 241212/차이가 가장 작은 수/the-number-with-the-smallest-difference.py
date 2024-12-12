
from sortedcontainers import SortedSet

s = SortedSet()

n, m = map(int, input().split())

nums = [int(input()) for _ in range(n)]

for i in nums:
    s.add(i)

ans = float('inf')

for i in nums:

    index = s.bisect_right(i)

    for j in range(3):

        index += j

        if not (0 <= index < len(s)):
            continue

        if abs(s[index] - i) >= m:
            ans = min(ans, abs(s[index] - i))
            break


print(ans if ans != float('inf') else -1)


