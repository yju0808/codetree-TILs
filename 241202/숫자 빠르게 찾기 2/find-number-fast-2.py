from sortedcontainers import SortedSet

s = SortedSet() 

n, m = map(int, input().split())
nums = list(map(int, input().split()))

for n in nums:
    s.add(n)


for _ in range(m):

    num = int(input())

    index = s.bisect_left(num)

    if index < len(s):
        print(s[index])
    else:
        print(-1)

