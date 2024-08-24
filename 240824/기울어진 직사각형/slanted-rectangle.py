N = int(input())

grid = [list(map(int, input().split())) for _ in range(N)]


dy = [1, -1, -1, 1]
dx = [1, 1, -1, -1]

def is_vaild_coord(y, x):
    return 0 <= y < N and 0 <= x < N 




def cal_score(y, x, h, w):

    result = 0
    move = [w, h, w, h]

    for i in range(4):
        for _ in range(move[i]):
            y += dy[i]
            x += dx[i]

            if not is_vaild_coord(y, x):
                return 0
            
            result += grid[y][x]
    
    return result

        
    
    

ans = 0


for i in range(N):
    for j in range(N):
        for h in range(1, N):
            for w in range(1, N):

                ans = max(ans, cal_score(i, j, h, w))

print(ans)