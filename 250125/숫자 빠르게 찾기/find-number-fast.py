

n, m = map(int, input().split())

nums = list(map(int, input().split()))

def binary_search(target):

    left = 0
    right = n - 1

    while left <= right:

        mid = (left + right) // 2

        if nums[mid] == target:
            return mid

        if nums[mid] > target:
            right = mid - 1
        
        elif nums[mid] < target:
            left = mid + 1

    return -1


for _ in range(m):

    target = int(input())

    res = binary_search(target)

    print(res + 1 if res != -1 else res)