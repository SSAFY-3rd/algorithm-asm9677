import sys
input = sys.stdin.readline
INF = 1<<30

n,m = map(int, input().split())
dist = [[INF]*(n+1) for i in range(n+1)]
res = [[0]*(n+1) for i in range(n+1)]

for _ in range(m):
    a,b,c = map(int, input().split())    
    dist[a][b] = dist[b][a] = min(dist[a][b], c)
    res[a][b],res[b][a] = b,a

for k in range(1,n+1):
    for i in range(1,n+1):
        if i == k: continue
        for j in range(1,n+1):
            if j == i or j == i: continue
            if dist[i][j] > dist[i][k] + dist[k][j]:
                dist[i][j] = dist[j][i] = dist[i][k] + dist[k][j]
                res[i][j], res[j][i] = res[i][k], res[j][k]
                
for i in range(1,n+1):
    print(*['-' if res[i][j] == 0 else res[i][j] for j in range(1,n+1)])