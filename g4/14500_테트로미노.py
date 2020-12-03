n,m = map(int, input().split())
arr = [[0]*(m+4) for i in range(2)] + [[0]*2 + [*map(int, input().split())] + [0]*2 for i in range(n)] + [[0]*(m+4) for i in range(2)]

res = 0
for i in range(2, n+2):
    for j in range(2, m+2):
        hBlock = sum(sorted([arr[i-1][j], arr[i-1][j+1], arr[i][j-1], arr[i][j+2], arr[i+1][j], arr[i+1][j+1]], reverse=True)[:2]) + arr[i][j+1]
        vBlock = sum(sorted([arr[i-1][j], arr[i][j-1], arr[i][j+1], arr[i+1][j-1], arr[i+1][j+1], arr[i+2][j]], reverse=True)[:2]) + arr[i+1][j]
        res = max(res, max(hBlock, vBlock) + arr[i][j])
print(res)