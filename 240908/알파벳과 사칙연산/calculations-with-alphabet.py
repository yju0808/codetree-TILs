string = input()

count = 0
nums = [str(i + 1) for i in range(4)]
selected_nums = []

for s in string:
    if s.isalpha():
        count += 1


def cal(string, nums):

    i = 0
    current = 0
    new_string = []

    for s in string:

        if s.isalpha():
            new_string.append(int(nums[i]))
            i += 1
        else:
            new_string.append(s)

    for i in range(0, len(new_string)):

        s = new_string[i]

        if s == '*':
            current += new_string[i - 1] * new_string[i + 1]

        elif s == '-':
            current += new_string[i - 1] - new_string[i + 1]

        elif s == '+':
            current += new_string[i - 1] + new_string[i + 1]

    return current


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