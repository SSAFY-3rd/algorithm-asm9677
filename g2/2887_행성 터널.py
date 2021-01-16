from heapq import *
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**5)

def find(u):
    if parent[u] == u: return u
    parent[u] = find(parent[u])
    return parent[u]

n = int(input())
parent = [i for i in range(n)]
pos = [[*map(int, input().split())] for i in range(n)]
x,y,z = [*sorted((pos[i][0],i) for i in range(n))],[*sorted((pos[i][1],i)for i in range(n))],[*sorted((pos[i][2],i) for i in range(n))]

hq = []
for i in range(1,n):
    heappush(hq, [abs(x[i][0] - x[i-1][0]), x[i-1][1], x[i][1]])
    heappush(hq, [abs(y[i][0] - y[i-1][0]), y[i-1][1], y[i][1]])
    heappush(hq, [abs(z[i][0] - z[i-1][0]), z[i-1][1], z[i][1]])

res = 0
while n != 1:
    d,u,v = heappop(hq)
    u,v = find(u), find(v)
    if u != v:
        parent[u] = v
        res += d
        n -= 1
print(res)