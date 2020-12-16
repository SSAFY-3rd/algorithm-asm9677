import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

def dfs(cur):
    for next in adj[cur]:
        if state[next] == state[cur]:
            return 0
        if not state[next]:
            state[next] = 3 - state[cur]
            if not dfs(next): return 0        
    return 1

n,m = map(int, input().split())
adj = [[] for i in range(n+1)]

for i in range(m):
    a,b = map(int, input().split())
    adj[a] += [b]
    adj[b] += [a]

state = [0]*(n+1)
res = 1
for i in range(1,n+1):
    if not state[i]:
        state[i] = 1
        if not dfs(i):
            res = 0
            break
print(res)
