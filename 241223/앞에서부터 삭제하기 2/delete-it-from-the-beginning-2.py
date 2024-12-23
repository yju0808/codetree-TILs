import heapq as hq

n = int(input())

nums = list(map(int, input().split()))
min_heap = []
count = dict()

current_sum = sum(nums)
current_len = len(nums)

ans = 0

for k in nums:
    hq.heappush(min_heap, k)
    
    if k in count:
        count[k] += 1
    else:
        count[k] = 1


for i in range(0, n -2):

    current_sum -= nums[i]
    count[nums[i]] -= 1
    current_len -= 1


    min_value = hq.heappop(min_heap)

    while count[min_value] <= 0:
        min_value = hq.heappop(min_heap)

    hq.heappush(min_heap, min_value)

    ans = max(ans, (current_sum - min_value) / (current_len - 1))

print(f"{ans:.2f}")

    



    

    




