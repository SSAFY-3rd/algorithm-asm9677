from collections import deque
import sys
input = sys.stdin.readline

dir = [[1,0],[0,1],[-1,0],[0,-1]]

N,M,P = map(int, input().split())
S = [0] + [*map(int, input().split())]
tmp = [input() for i in range(N)]

que = [deque() for i in range(P+1)]
res = [0]*(P+1)
visited = [[0]*M for i in range(N)]

for i in range(N):
    for j in range(M):
        if '0' <= tmp[i][j] <= '9':
            num = int(tmp[i][j])
            que[num] += [(i,j)]
            res[num] += 1
            visited[i][j] = True          
        elif tmp[i][j] == '#':
            visited[i][j] = True

while True:    
    actives = 0
    for p in range(1,P+1):       
        actives += len(que[p]) != 0
        for s in range(S[p]):   
            cnt = len(que[p])
            if cnt == 0: break
            for _ in range(cnt):
                i,j = que[p].popleft()
                for dy,dx in dir:
                    ni,nj = i + dy, j + dx
                    if 0 <= ni < N and 0 <= nj < M and not visited[ni][nj]:
                        visited[ni][nj] = True
                        res[p] += 1
                        que[p].append((ni,nj))
            # else:
            #     break
    if not actives:
        break
print(*res[1:])