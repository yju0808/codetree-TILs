

import heapq as hq


n = int(input())
min_heap = []


for _ in range(n):

    k = int(input())

    if k == 0:

        if min_heap:
            abs_value, value = hq.heappop(min_heap) 
            print(value)
        else:
            print(0)

    else:
        hq.heappush(min_heap, (abs(k), k))


