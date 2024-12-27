
import heapq as hq

n = int(input())

nums = list(map(int, input().split()))

min_heap = []


for k in nums:

    hq.heappush(min_heap, k)

    if len(min_heap) < 3:
        print(-1)
        continue

    a1 = hq.heappop(min_heap)
    a2 = hq.heappop(min_heap)
    a3 = hq.heappop(min_heap)

    print(a1 * a2 * a3)

    hq.heappush(min_heap, a1)
    hq.heappush(min_heap, a2)
    hq.heappush(min_heap, a3)

