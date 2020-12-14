import sys
input = sys.stdin.readline 

dir = [[0,0],[-1,0],[1,0],[0,-1],[0,1]]
n,m,k = map(int, input().split())
arr = [[*map(int, input().split())] for i in range(n)]
scent = [[[arr[i][j], k if arr[i][j] else 0] for j in range(n)] for i in range(n)]

sharkDir = [0] + [*map(int, input().split())]
priority = [[] for i in range(m+1)]
for i in range(1,m+1):
    priority[i].append([])
    for j in range(4):
        priority[i].append([*map(int, input().split())])

res = 0
while res <= 1000 and sum(arr[i][j] for j in range(n) for i in range(n)) != 1:    
    new_arr = [[0]*n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                sNum, sDir = arr[i][j], sharkDir[arr[i][j]]
                si,sj,sd,flag = -1,-1,-1,True
                for d in priority[sNum][sDir]:
                    ni,nj = i + dir[d][0],  j + dir[d][1]
                    if 0 <= ni < n and 0 <= nj < n:
                        if scent[ni][nj][0] == sNum and si == -1:
                            si,sj,sd = ni,nj,d
                        if scent[ni][nj][0] != 0:
                            continue

                        new_arr[ni][nj] = min(new_arr[ni][nj], sNum) if new_arr[ni][nj] != 0 else sNum
                        sharkDir[sNum] = d                        
                        flag = False
                        break
                if flag:
                    new_arr[si][sj],sharkDir[sNum] = sNum,sd

    arr = new_arr
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
               scent[i][j] = [arr[i][j], k] 
            elif scent[i][j][1] <= 1:
                scent[i][j] = [0,0]
            else:
                scent[i][j][1] -= 1
    res += 1
print(res if res <= 1000 else -1)