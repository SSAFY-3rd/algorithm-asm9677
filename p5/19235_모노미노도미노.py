import sys
input = sys.stdin.readline
N,M = 6,4
dir = [[1,0],[0,1],[-1,0],[0,-1]]

def addBlock(arr,num,t,k):
    if t == 1: r1,c1 = r2,c2 = 0,k
    elif t == 2: r1,c1,r2,c2 = 0,k,0,k+1
    else: r1,c1,r2,c2 = 0,k,1,k
    
    while r1 < N and r2 < N and not arr[r1][c1] and not arr[r2][c2]:
        r1 += 1; r2 += 1
    r1 -= 1; r2 -= 1
    arr[r1][c1] = arr[r2][c2] = num    

    while removeBlock(arr):
        alignBlock(arr)

    while arr[1].count(0) != 4:
        arr[N-1] = [0]*M 
        alignBlock(arr)
    return score

def alignBlock(arr):    
    for x in range(N-1, -1, -1):
        for y in range(M):                        
            if arr[x][y] == 0: continue

            num = arr[x][y]
            r1,c1 = r2,c2 = x,y

            for d in range(4):
                nx,ny = x + dir[d][0], y + dir[d][1]
                if 0 <= nx < N and 0 <= ny < M and arr[x][y] == arr[nx][ny]:
                    r2,c2 = nx,ny

            arr[r1][c1] = arr[r2][c2] = 0
            while r1 < N and r2 < N and arr[r1][c1]  == 0 and arr[r2][c2] == 0:
                r1 += 1; r2 += 1
            r1 -= 1; r2 -= 1
            arr[r1][c1] = arr[r2][c2] = num

def removeBlock(arr):
    global score
    flag = False
    for i in range(N-1, -1, -1):
        if arr[i].count(0) == 0:
            arr[i] = [0]*M            
            flag = True
            score += 1        
    return flag

n = int(input())
blue = [[0]*M for i in range(N)]
green = [[0]*M for i in range(N)]
score = 0

for i in range(1,n+1):
    t,x,y = map(int, input().split())        
    addBlock(blue, i, t if t == 1 else (3 if t == 2 else 2), x)
    addBlock(green, i, t, y)

print(score)
print(sum((blue[i][j] != 0) + (green[i][j] != 0) for j in range(M) for i in range(N)))