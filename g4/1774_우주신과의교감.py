import sys
input = sys.stdin.readline

def find(parent, u):
    stack = []
    while parent[u] != u:
        stack += [u]
        u = parent[u]
    for c in stack:
        parent[c] = u
    return u

def solve(parent):    
    pos = [[*map(int,input().split())] for i in range(n)]
    dist = []
    for i in range(n):
        for j in range(i+1,n):            
            x1,y1,x2,y2 = *pos[i],*pos[j]
            dist.append([((x1-x2)**2 + (y1-y2)**2)**0.5, i,j])
    dist.sort()

    for _ in range(m):
        u,v = map(int, input().split())
        pu,pv = find(parent, u-1), find(parent, v-1)    
        if pu != pv: parent[pu] = pv

    res = 0
    for d,u,v in dist:
        pu,pv = find(parent, u), find(parent, v)    
        if pu != pv: 
            parent[pu] = pv
            res += d
    return res

n,m = map(int, input().split())
print(format(solve([i for i in range(n)]), '.2f'))