from sortedcontainers import SortedDict

sd = SortedDict()


n = int(input())

for i in range(n):

    inputs = input().split()

    command = inputs[0]

    if command == 'add':
        key, value = int(inputs[1]), int(inputs[2])

        sd[key] = value

    elif command == 'remove':
        key = int(inputs[1])
        sd.pop(key)

    elif command == 'find':
        key = int(inputs[1])

        if key in sd:
            print(sd[key])
        else:
            print('None')


    elif command == 'print_list':

        if len(sd) == 0:
            print('None')

        else:
            for key, value in sd.items():
                print(value,end = ' ')
            print()