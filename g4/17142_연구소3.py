import sys,queue
from itertools import combinations
In = sys.stdin.readline

INF = 987654321
n, m = map(int, In().split())
arr = [[*map(int, In().split())] for i in range(n)]
dir = [(1,0),(0,1),(-1,0),(0,-1)]

virus_pos = []
cnt = 0

for i in range(n):
    for j in range(n):
        if arr[i][j] == 2:
            virus_pos += [(i,j)]
            arr[i][j] = INF
        elif arr[i][j] == 0:
            arr[i][j] = INF
            cnt += 1
        else:
            arr[i][j] = -1
if cnt == 0:
    print(0)
else:         
    visited = [[[arr[i][j] for j in range(n)] for i in range(n)] for k in range(len(virus_pos))]    
    for k in range(len(virus_pos)):        
        q = queue.Queue()
        q.put(virus_pos[k])

        cnt = 0          
        while not q.empty():
            size = q.qsize()
            for i in range(size):                
                r,c = q.get()       
                for d in range(4):
                    nr = r + dir[d][0]
                    nc = c + dir[d][1]
                    if nr > -1 and nr < n and nc > - 1 and nc < n and visited[k][nr][nc] == INF:   
                        visited[k][nr][nc] = cnt+1
                        q.put((nr, nc))
            cnt += 1
        for r,c in virus_pos:
            visited[k][r][c] = 0       

    result = INF
    for index in combinations(range(len(virus_pos)), m):
        mx,mn = -INF,INF
        for i in range(n):
            for j in range(n):
                if arr[i][j] == -1: continue
                mn = INF
                for k in index:                    
                    if mn > visited[k][i][j]:
                        mn = visited[k][i][j]
                if mx < mn:
                    mx = mn

                if mx >= result:
                    break
            if mx >= result:
                break
        if result > mx:
            result = mx
            
    print(result if result != INF else -1)