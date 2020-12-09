from collections import deque
import sys
input = sys.stdin.readline
INF = 1<<30
dir = [[1,0],[0,1],[-1,0],[0,-1]]

def bfs(pos):
    dq = deque(pos)
    count = [[INF]*m for i in range(n)]
    for r,c,k in dq:
        count[r][c] = k

    while dq:
        for _ in range(len(dq)):
            r,c,k = dq.popleft()
            
            for d in range(4):
                nr,nc,nk = r + dir[d][0], c + dir[d][1],k                
                if 0 <= nr < n and 0 <= nc < m and arr[nr][nc] != 1:
                    if arr[nr][nc] == 2: nk += 1
                    if nk < count[nr][nc]:
                        count[nr][nc] = nk
                        dq.append((nr,nc,nk))
    return count

n,m = 0,0
for _ in range(int(input())):
    n,m = map(int, input().split())
    tmp = [' '.join(input()).split() for i in range(n)]
    arr = [[0]*m for i in range(n)]
    pos,exitPos = [],[]
    
    for i in range(n):
        for j in range(m):
            if tmp[i][j] == '*':
                arr[i][j] = 1
            elif tmp[i][j] == '#':
                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    exitPos += [(i,j,1)]
                arr[i][j] = 2
            elif tmp[i][j] == '$':                                
                pos += [(i,j)]

            if tmp[i][j] == '$' or tmp[i][j] == '.':
                if i == 0 or j == 0 or i == n-1 or j == m-1:
                    exitPos += [(i,j,0)]
            
    r1,c1,r2,c2 = *pos[0],*pos[1]    
    count1 = bfs([(*pos[0],0)])
    count2 = bfs([(*pos[1],0)])
    count3 = bfs(exitPos)

    res = count3[r1][c1] + count3[r2][c2]
    for i in range(n):
        for j in range(m):
            if arr[i][j] == 2:
                res = min(res,count1[i][j] + count2[i][j] + count3[i][j] - 2)                
    print(res)

