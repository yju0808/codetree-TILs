a = input()


def encode(a):

    temp = a[0]

    result = ''
    count = 0

    for c in a:

        if c != temp:
            result += c
            result += str(count)
            count = 0
            temp = c
        else:
            count += 1

    if count != 0:
        result += c
        result += str(count)

    return result


def shift(a, n):
    
    after = ['' for _ in range(len(a))]

    for i in range(0, len(a) - n):
        after[i + n] = a[i]

    for i in range(0, n):
        after[i] = a[len(a) - n + i - 1]

    return "".join(after)


ans = float('inf')


for i in range(len(a)):
    
    result = encode(shift(a, i))
    ans = min(ans, len(result))


print(ans)