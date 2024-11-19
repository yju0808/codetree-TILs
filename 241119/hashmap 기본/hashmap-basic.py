

d = dict()

n = int(input())

for i in range(n):

    inputs = input().split()

    c = inputs[0]

    o1 = int(inputs[1])

    if c == 'add':
        o2 = int(inputs[2])
        d[o1] = o2

    elif c == 'find':
        if o1 in d:
            print(d[o1])
        else:
            print('None')

    elif c == 'remove':
        del d[o1]