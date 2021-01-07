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
    cnt = 0
    for _ in range(m):
        cnt += 1
        u,v = map(int, input().split())
        pu,pv = find(parent, u), find(parent, v)    
        if pu == pv: return cnt
        parent[pu] = pv
    return 0

n,m = map(int, input().split())
print(solve([i for i in range(n)]))