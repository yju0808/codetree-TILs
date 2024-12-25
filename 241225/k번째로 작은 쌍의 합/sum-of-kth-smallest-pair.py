
import heapq as hq

n, m, k = map(int, input().split())

nums_n = list(map(int, input().split()))

nums_m = list(map(int, input().split()))

nums_n.sort()
nums_m.sort()

min_heap = []


for i in range(len(nums_n)):
    hq.heappush(min_heap, (nums_n[i] + nums_m[0], i, 0))

for _ in range(k - 1):
    pair_sum, i, j = hq.heappop(min_heap)

    j += 1

    if j < m:
        hq.heappush(min_heap, (nums_n[i] + nums_m[j], i, j))


pair_sum, i, j = hq.heappop(min_heap)

print(pair_sum)
