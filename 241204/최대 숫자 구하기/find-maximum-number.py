from sortedcontainers import SortedSet


s = SortedSet()

n, m = map(int, input().split())


for i in range(1, m + 1):
    s.add(i)


inputs = list(map(int, input().split()))

for i in inputs:

    s.remove(i)
    print(s[-1])