from sortedcontainers import SortedSet


n, m = map(int, input().split())

del_nums = list(map(int, input().split()))
s = SortedSet()
section = SortedSet()
section.add((-(n + 1), -1, n + 1))

s.add(-1)
s.add(n + 1)

for n in del_nums:

    s.add(n)

    index = s.bisect_left(n)



    can1 = s[index + 1] # 큰 
    can2 = s[index - 1] # 작은 

    section.remove((-(can1- can2 - 1), can2, can1))
    section.add((-(n - can2 - 1), can2, n))
    section.add((-(can1 - n - 1), n, can1))
    ans = 0
    ans, _, _ = section[0]
    print(-ans)

    



