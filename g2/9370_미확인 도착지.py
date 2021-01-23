import sys
from heapq import heappop,heappush
input = sys.stdin.readline

for T in range(int(input())):    
    hq = []
    n,m,t = map(int, input().split())
    s,g,h = map(int, input().split())
    adj = [[] for i in range(n+1)]
    
    for i in range(m):
        a,b,d = map(int,input().split())
        adj[a] += [(b,d)]
        adj[b] += [(a,d)]

    dest = set(int(input()) for i in range(t))
    
    visited = [987654321]*(n+1)    
    heappush(hq, (0, s))
    visited[s] = 0
    while hq:
        cost,node = heappop(hq)
        if visited[node] < cost:
            continue

        for next,d in adj[node]:
            nCost = cost+d
            if visited[next] > nCost:
                visited[next] = nCost
                heappush(hq, (nCost, next))

    node = []
    if visited[g] > visited[h]:
        node += [g]
    else:
        node += [h]
    
    trace = [node[-1]]    
    visited2 = [0]*(n+1)
    visited2[node[-1]] = 1
    while node:
        cur = node.pop()
        
        for next,d in adj[cur]:
            if not visited2[next] and visited[next] == visited[cur]+d:
                visited2[next] = 1
                node += [next]
                trace += [next]
    res = []
    for k in sorted(trace):
        if k in dest:
            res += [k]
    print(*res)