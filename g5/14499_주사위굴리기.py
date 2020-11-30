dir = [[0,0],[0,1],[0,-1],[-1,0],[1,0]]
dice = [[0,0,0,0] for i in range(2)]

n,m,x,y,k = map(int, input().split())
arr = [[*map(int, input().split())] for i in range(n)]

for k in map(int, input().split()):    
    nx,ny = x+dir[k][0], y+dir[k][1]
    if nx < 0 or nx >= n or ny < 0 or ny >= m:
        continue    
    x,y = nx,ny

    i,d = k <= 2, dir[k][0] or dir[k][1]
    dice[i] = dice[i][d:] + dice[i][0:d]
    dice[(i+1)%2][1::2] = dice[i][1::2]

    if arr[x][y] == 0:
        arr[x][y] = dice[0][-1]
    else:
        dice[0][-1] = dice[1][-1] = arr[x][y]
        arr[x][y] = 0

    print(dice[0][1])