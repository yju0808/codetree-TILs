import heapq as hq

t = int(input())


for _ in range(t):

    min_heap = []
    max_heap = []

    n = int(input())

    nums = list(map(int, input().split()))

    hq.heappush(max_heap, -nums[0])

    print(nums[0], end = ' ')

    for i in range(1, len(nums)):

        # 상단에 넣을 차례
        if i % 2 == 1:
            
            if nums[i] < -max_heap[0]:
                temp = -hq.heappop(max_heap)
                hq.heappush(min_heap, temp)
                hq.heappush(max_heap, -nums[i])

            else: 
                hq.heappush(min_heap, nums[i])

        # 하단에 넣을 차례 + 출력할 차례
        else:
            
            if nums[i] > min_heap[0]:
                temp = hq.heappop(min_heap)
                hq.heappush(max_heap, -temp)
                hq.heappush(min_heap, nums[i])
        
            else:
                hq.heappush(max_heap, -nums[i])

            print(-max_heap[0], end = ' ')
    
    print()


    









