import sys
input = sys.stdin.readline

def find(v):
    if parent[v] == v:
        return v
    parent[v] = find(parent[v])
    return parent[v]

def solve(n,m):
    arr = [[*map(int,input().split())] for i in range(n)]
    trace = [*map(int,input().split())]
    global parent
    parent = [i for i in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i][j]:
                u,v = find(i), find(j)
                parent[u] = parent[v]
    return [find(v-1) for v in trace].count(find(trace[0]-1)) == m 
print('YES' if solve(int(input()),int(input())) else 'NO')