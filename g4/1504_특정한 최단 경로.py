from heapq import *
import sys

input = sys.stdin.readline
INF = 1<<31

def dijkstra(u,v):
    dist = [INF]*(n+1)
    dist[u] = 0

    hq = [(0,u)]
    while hq:
        d,node = heappop(hq)
        
        if dist[node] < d:
            continue
        if node == v:
            return d

        for next,cost in adj[node]:
            nCost = cost + d
            if nCost < dist[next]:
                dist[next] = nCost
                heappush(hq, (nCost, next))
    return INF
    
n,m = map(int, input().split())
adj = [[] for i in range(n+1)]

for i in range(m):
    a,b,c = map(int, input().split())
    adj[a] += [[b,c]]
    adj[b] += [[a,c]]

v1,v2 = map(int, input().split())

res = min(dijkstra(1,v1) + dijkstra(v1,v2) + dijkstra(v2,n), dijkstra(1,v2) + dijkstra(v2,v1) + dijkstra(v1,n))
print(res if res < INF else -1)