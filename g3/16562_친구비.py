import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(cur):
    mn = pay[cur]
    visited[cur] = 1    
    for next in adj[cur]:
        if not visited[next]:
            mn = min(mn, dfs(next))
    return mn

n,m,k = map(int, input().split())

pay = [0]+[*map(int, input().split())]
adj = [[] for i in range(n+1)]
visited = [0]*(n+1)

for _ in range(m):
    a,b = map(int, input().split())
    adj[a] += [b]
    adj[b] += [a]

res = sum(dfs(i) for i in range(1,n+1) if not visited[i])
print(res if res <= k else 'Oh no')