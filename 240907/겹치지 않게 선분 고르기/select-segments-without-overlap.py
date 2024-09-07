n = int(input())

points = [tuple(map(int, input().split())) for _ in range(n)]
selected = []


def is_overlapped(points):
    
    visited = set()


    for x1, x2 in points:

        for x in range(x1, x2 + 1):
            if x in visited:
                return True
            visited.add(x)

    return False

ans = 0

def select():

    global ans

    if len(selected) == len(points):
        return


    for i in range(len(points)):

        selected.append(points[i])

        if (is_overlapped(selected)):
            return
        else:
            ans = len(selected)

        select()
        selected.pop()

select()

print(ans)