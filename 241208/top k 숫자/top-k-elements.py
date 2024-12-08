


from sortedcontainers import SortedSet


s = SortedSet()


n, m = map(int, input().split())
nums = list(map(int, input().split()))

for n in nums:
    s.add(n)

length = len(s)

for i in range(0, m):
    print(s[length - i - 1], end = ' ')