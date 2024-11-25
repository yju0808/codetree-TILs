from sortedcontainers import SortedDict

sd = SortedDict() 

n = int(input())
nums = list(map(int, input().split()))
nums.insert(0, 0)

for i in range(1, n + 1):

    num = nums[i]

    if num not in sd:
        sd[num] = i


for key, value in sd.items():
    print(key, value)