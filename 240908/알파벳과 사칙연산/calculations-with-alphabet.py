string = input()

count = set()
nums = [str(i + 1) for i in range(4)]
selected_nums = []


for s in string:
    if s.isalpha():
        count.add(s)



def cal(string, nums):

    prefix = []
    ops = []
    i = 0
    stack = []
    mapper = {}

    for s in string:
        if s.isalpha() and s not in mapper:
            mapper[s] = nums[i]
            i += 1


    for s in string:

        if s.isalpha():
            prefix.append(mapper[s])
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

    if k == len(count):
        ans = max(ans, cal(string, selected_nums))
        return

    for num in nums:
        selected_nums.append(num)
        select(k + 1)
        selected_nums.pop()


select(0)
print(ans)