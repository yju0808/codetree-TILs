
import heapq as hq


n = int(input())

nums = list(map(int, input().split()))
min_heap = []

for num in nums:
    hq.heappush(min_heap, num)

ans = 0

while len(min_heap) > 1:
    m1 = hq.heappop(min_heap)
    m2 = hq.heappop(min_heap)

    ans += m1 + m2
    hq.heappush(min_heap, m1 + m2)



print(ans)