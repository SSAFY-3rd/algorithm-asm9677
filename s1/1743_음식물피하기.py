import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

def dfs(r,c):
    arr[r][c] = 0
    ret = 1
    for d in range(4):
        nr,nc = r + dir[d][0], c + dir[d][1]
        if nr >= 0 and nr < n and nc >= 0 and nc < m and arr[nr][nc]:
            ret += dfs(nr,nc)
    return ret

dir = [[1,0],[-1,0],[0,1],[0,-1]]
n,m,k = map(int, input().split())
arr = [[0]*m for i in range(n)]

for i in range(k):
    r,c = map(int,input().split())
    arr[r-1][c-1] = 1

res = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]:
            res = max(res,dfs(i,j))
print(res)