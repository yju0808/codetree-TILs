n = int(input())

nums = [i for i in range(1, n + 1)]
selected = []

visitied = [False for _ in range(n)]

def solve(last):

    if len(selected) == n:
        print(*selected)
        return


    for i in range(n - 1, -1, -1):

        if visitied[i]:
            continue

        selected.append(nums[i])
        visitied[i] = True

        solve(i)

        selected.pop()
        visitied[i] = False


solve(-1)