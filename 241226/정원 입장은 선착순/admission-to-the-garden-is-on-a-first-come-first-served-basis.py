
import heapq as hq

n = int(input())


min_heap = []

min_heap_another = []

for i in range(n):
    a, t = map(int, input().split())

    hq.heappush(min_heap, (a, i, t))


ans = 0
current_time = min_heap[0][0]


while min_heap:

    current_time = max(current_time, min_heap[0][0])

    while min_heap and min_heap[0][0] <= current_time:
        a, i, t = hq.heappop(min_heap)
        hq.heappush(min_heap_another, (i, a, t))
    
    while min_heap_another:

        i, a, t = hq.heappop(min_heap_another)

        current_time = max(current_time, a)
        ans = max(ans, abs(current_time - a))
        current_time = current_time + t

        if min_heap and min_heap[0][0] <= current_time:
            break



print(ans)



    





