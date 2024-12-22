import heapq as hq


n = int(input())

min_heap = []

nums = list(map(int, input().split()))

for n in nums:
    hq.heappush(min_heap, -n)

while len(min_heap) >= 2:

    first = -hq.heappop(min_heap)
    second = -hq.heappop(min_heap)

    new = first - second

    if new:
        hq.heappush(min_heap, - new)


if min_heap:
    print(-min_heap[0])
else:
    print(-1)