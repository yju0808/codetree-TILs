
n, k = map(int, input().split())

nums = list(map(int, input().split()))

d = dict()
ans = 0

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):

        n1 = nums[i]
        n2 = nums[j]

        target = k - (n1 + n2)

        if target in d:
            ans += d[target]

        if n1 + n2 in d:
            d[n1 + n2] += 1
        else:
            d[n1 + n2] = 1


print(ans)
