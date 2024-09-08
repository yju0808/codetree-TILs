n, m, c = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
selected_point = []


ans = 0

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


def cal_score(nums):

    result = 0

    if sum(nums) > c:
        return 0

    for num in nums:
        result += num * num

    return result



def simul(p1, p2):

    global ans

    if is_overlaped(p1, p2):
        return 0

    y1, x1 = p1
    y2, x2 = p2

    nums1 = []
    nums2 = []

    for i in range(x1, x1 + m):

        if i >= n:
            break

        nums1.append(grid[y1][i])

    for i in range(x2, x2 + m):

        if i >= n:
            break

        nums2.append(grid[y2][i])

    result = 0

    

    w1 = select(nums1, 0, 0)
    w2 = select(nums2, 0, 0)

    result = w1 + w2

    ans = max(ans, result)




def select(nums, k, max_weight):

    if k == len(nums):
        score = cal_score(selected_point)
        max_weight = max(score, max_weight)
        return max_weight

    
    selected_point.append(nums[k])

    max_weight = max(select(nums, k + 1, max_weight), max_weight)

    selected_point.pop()

    max_weight = max(select(nums, k + 1, max_weight), max_weight)

    return max_weight




def is_overlaped(p1, p2):

    y1, x1 = p1
    y2, x2 = p2

    if y1 != y2:
        return False

    right = max(x1, x2)
    left = min(x1, x2)

    if left + m - 1 >= right:
        return True

    return False



for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                simul((i, j), (k, l))


print(ans)