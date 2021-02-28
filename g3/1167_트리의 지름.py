import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def solve(v):
    global res
    visited[v] = 1

    l = 0
    for next,c in adj[v]:
        if visited[next]: continue
        r = solve(next)+c
        res = max(res, l+r)
        l = max(l, r)
    return l

n=int(input())
adj = [[] for i in range(n+1)]
visited = [0]*(n+1)
res = 0

for i in range(n):
    temp = [*map(int,input().split())]
    cur = temp[0]
    for j in range(1, len(temp)-1, 2):
        adj[cur] += [temp[j:j+2]]

solve(1)
print(res)