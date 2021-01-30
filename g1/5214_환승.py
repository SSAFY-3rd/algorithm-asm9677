import sys
input = sys.stdin.readline

def solve(N,K,M):
    adj = [[] for i in range(N+1)]
    hyper = [[*map(int, input().split())] for i in range(M)]

    for i in range(M):
        for k in hyper[i]:
            adj[k] += [i]

    q = [1]
    visited = [0]*(N+1)
    visited[1] = 1

    res,cnt = -1,1
    while q and res == -1:
        tq = []
        for _ in range(len(q)):
            cur = q.pop()
            if cur == N:
                res = cnt
                break
            
            for idx in adj[cur]:
                for next in hyper[idx]:
                    if not visited[next]:
                        visited[next] = 1
                        tq.append(next)
                hyper[idx] = []
        q = tq
        cnt += 1
    return res
print(solve(*map(int, input().split())))