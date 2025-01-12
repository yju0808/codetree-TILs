




from functools import cmp_to_key

n = int(input())

nums = [int(input()) for _ in range(n)]


def compare(x, y):

    new_x = int(str(x) + str(y))
    new_y = int(str(y) + str(x))

    if new_x > new_y:
        return -1

    if new_x < new_y:
        return 1

    return 0

nums.sort(key=cmp_to_key(compare))


for n in nums:
    print(n, end = '')