
n, k, b = map(int, input().split())


prefix_sum = [0 for _ in range(n)]
nums = [0 for _ in range(n)]

for _ in range(b):
    missing_num = int(input())
    missing_num -= 1
    nums[missing_num] = 1

prefix_sum[0] = nums[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i]


ans = float('inf')

for i in range(n - k + 1):
    temp = prefix_sum[i + k - 1] - prefix_sum[i] + nums[i]
    ans = min(ans, temp)

print(ans)

    


