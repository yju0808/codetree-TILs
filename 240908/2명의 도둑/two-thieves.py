n, m, c = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(n)]
selected_point = []

def is_valid_coord(y, x):
    return 0 <= y < n and 0 <= x < n


def simul(points):

    result = 0

    if is_overlaped(points):
        return 0

    for y, x in points:

        for i in range(x, x + m):
            
    
    pass



def is_overlaped(points):

    for i in range(len(points)):

        for j in range(len(points)):

            if i == j:
                continue

            y1, x1 = points[i]
            y2, x2 = points[j]

            if y1 == y2:

                left = min(x1, x2)
                right = max(x1, x2)
                
                if left + m - 1 >= right
                    return True
    return False


for i in range(n):
    for j in range(n):
        for k in range(n):
            for l in range(n):
                pass








select(0, 0)