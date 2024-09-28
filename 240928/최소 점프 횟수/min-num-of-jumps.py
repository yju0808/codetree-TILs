n = int(input())

nums = list(map(int, input().split()))

ans = float('inf')

def solve(current, count):

    global ans

    if current >= n:
        return

    if current == n - 1:
        ans = min(ans, count)
        return


    for i in range(1, nums[current] + 1):
        solve(current + i, count + 1)
        

solve(0, 0)
print(ans if ans != float('inf') else - 1)