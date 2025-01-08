
n = int(input())

nums = list(map(int, input().split()))

prefix_sum = [0 for _ in range(n)]
prefix_sum[0] = nums[0]

for i in range(1, n):
    prefix_sum[i] = prefix_sum[i - 1] + nums[i]

ans = nums[0]
start = 0

for end in range(0, n):

    current_sum = prefix_sum[end] - prefix_sum[start] + nums[start]

    if current_sum < 0:
        start = end + 1

    ans = max(current_sum, ans)

print(ans)

