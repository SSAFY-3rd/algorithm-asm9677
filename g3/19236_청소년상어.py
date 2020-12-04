import copy

N,dir = 4, [[-1,0],[-1,-1],[0,-1],[1,-1],[1,0],[1,1],[0,1],[-1,1]]

arr = [[] for i in range(N)]
pos = [(-1,-1) for i in range(N*N+1)]

def solve(i,j,d,cur):
    global arr, pos
    
    res = cur
    visited[cur] = True

    copyArr = copy.deepcopy(arr)
    copyPos = copy.deepcopy(pos)

    for fn in range(1, N*N+1):
        if visited[fn]: continue

        fi,fj = pos[fn]
        fd = arr[fi][fj][1]
        
        while True:            
            ci,cj = fi + dir[fd][0], fj + dir[fd][1]
            if 0 <= ci < N and 0 <= cj < N and not (ci == i and cj == j):
                break
            fd = (fd+1) % 8

        arr[fi][fj][1] = fd
        cn = arr[ci][cj][0]       

        arr[fi][fj], arr[ci][cj] = arr[ci][cj], arr[fi][fj]
        pos[fn],pos[cn] = pos[cn],pos[fn]
        
    while 0 <= i < N and 0 <= j < N:  
        sn,sd = arr[i][j]
        if sn != 0 and not visited[sn]:
            res = max(res, solve(i,j,sd,sn) + cur)            
        i,j = i+dir[d][0], j+dir[d][1]
    
    arr = copyArr
    pos = copyPos
    visited[cur] = False
    return res

for i in range(N):
    fish = [*map(int,input().split())]
    for j in range(0,N*2,2):
        arr[i] += [[fish[j],fish[j+1]-1]]
        pos[fish[j]] = (i,j//2)

sn,sd = arr[0][0]
visited = [False] * (N*N+1)
print(solve(0,0,sd,sn))