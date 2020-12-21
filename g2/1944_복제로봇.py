from collections import deque
import sys
input = sys.stdin.readline
INF = 10**9

dir = [[1,0],[0,1],[-1,0],[0,-1]]

def find(u):
    if union[u] == u:
        return u
    union[u] = find(union[u])
    return union[u]

def solve():        
    n,m = map(int, input().split())
    m += 1
    arr = [input() for i in range(n)]

    dist = [[[INF]*n for i in range(n)] for j in range(m)]
    dq = deque()
    pos = []
    cnt = 0
    for i in range(n):
        for j in range(n):
            if arr[i][j] == 'S' or arr[i][j] == 'K':
                dq.append((i,j,cnt))
                dist[cnt][i][j] = 0
                pos.append((i,j))
                cnt += 1

    r = 0
    while dq:
        for _ in range(len(dq)):
            i,j,k = dq.popleft()

            for dy,dx in dir:
                ni,nj = i + dy, j + dx
                if 0 <= ni < n and 0 <= nj < n and dist[k][ni][nj] == INF and arr[ni][nj] != '1':
                    dist[k][ni][nj] = r+1
                    dq.append((ni,nj,k))
        r += 1

    global union
    union = [i for i in range(m)]
    kruskal = []
    for u in range(m):
        for v in range(u+1,m):            
            ni,nj = pos[v]
            if dist[u][ni][nj] == INF: continue
            kruskal.append((dist[u][ni][nj],u,v))
    kruskal.sort()
    res = 0
    for d,u,v in kruskal:
        pu,pv = find(u), find(v)
        if pu != pv:
            union[pu] = pv
            res += d
            m -= 1         
    print(res if m == 1 else -1)

solve()