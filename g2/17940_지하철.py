from heapq import *
import sys
input = sys.stdin.readline
INF = 1<<30

n,m = map(int, input().split())
color = [int(input()) for _ in range(n)]
dist = [[*map(int, input().split())] for i in range(n)]
adj = [[] for i in range(n)]

for i in range(n):
    for j in range(n):
        if dist[i][j]:
            adj[i] += [[j,dist[i][j]]]

hq = [(0,0,0)]
visited = [(INF,INF)]*n

while hq:
    c,d,cur = heappop(hq)
    if cur == m:
        print(c, d)
        break
    if visited[cur] < (c,d): continue
    for next,cost in adj[cur]:
        nc,nd = c + (color[cur] != color[next]), d + cost
        if visited[next] > (nc,nd):
            visited[next] = (nc,nd)
            heappush(hq, (nc,nd,next))

