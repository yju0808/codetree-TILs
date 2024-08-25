a = input()


def encode(string):

    temp = string[0]

    result = ''
    count = 0

    for c in string:

        if c != temp:
            result += temp
            result += str(count)
            count = 1
            temp = c
        else:
            count += 1

    if count != 0:
        result += c
        result += str(count)

    return result


def shift(a, n):
    
    after = ['_' for _ in range(len(a))]
    for i in range(0, len(a) - n):
        after[i + n] = a[i]

    for i in range(0, n):
        after[i] = a[len(a) - n + i]

    return "".join(after)


ans = float('inf')


for i in range(len(a) + 1):
    result = encode(shift(a, i))
    ans = min(ans, len(result))

print(ans)