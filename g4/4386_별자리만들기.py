import sys
input = sys.stdin.readline

def find(u):
    if parent[u] == u:
        return u
    parent[u] = find(parent[u])
    return parent[u]

n = int(input())
arr = [[*map(float, input().split())] for i in range(n)]
parent = [i for i in range(n)]
dist = []
for i in range(n):
    x1,y1 = arr[i]
    for j in range(i+1,n):
        x2,y2 = arr[j]
        dist.append((((x1-x2)**2 + (y1-y2)**2)**0.5,i,j))
dist.sort()

r = 0
for d,i,j in dist:
    u,v = find(i), find(j)
    if u != v:
        parent[u] = v
        r += d

print(round(r,2))