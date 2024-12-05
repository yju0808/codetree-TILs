

from sortedcontainers import SortedSet


s = SortedSet()

n = int(input())

nums = list(map(int, input().split()))


ans = float('inf')
s.add(0)

for n in nums:

    s.add(n)
    candi_index = s.bisect_left(n)


    if candi_index - 1 >= 0:
        ans = min(ans, abs(s[candi_index] - s[candi_index - 1]))

    if candi_index + 1 < len(s):
        ans = min(ans, abs(s[candi_index] - s[candi_index + 1]))


    print(ans)