string = input()

count = 0
nums = [str(i + 1) for i in range(4)]
selected_nums = []

for s in string:
    if s.isalpha():
        count += 1


def cal(string, nums):

    prefix = []
    ops = []
    i = 0
    stack = []

    for s in string:

        if s.isalpha():
            prefix.append(nums[i])
            i += 1
        else:
            ops.append(s)

    for op in ops:
        prefix.append(op)


    for s in prefix:
        if s.isdigit():
            stack.append(int(s))
        else:
            p1 = stack.pop()
            p2 = stack.pop()

            if s == '*':
                stack.append(p1 * p2)

            elif s == '-':
                stack.append(p1 - p2)

            elif s == '+':
                stack.append(p1 + p2)

    return stack[0]


ans = -float('inf')


def select(k):
    global ans 

    if k == count:
        ans = max(ans, cal(string, selected_nums))
        return

    for num in nums:
        selected_nums.append(num)
        select(k + 1)
        selected_nums.pop()


select(0)
print(ans)