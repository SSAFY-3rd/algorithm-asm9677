import sys
input = sys.stdin.readline

def solve(i,j,k,f):
    if k == 0:
        return 0
    if j >= m:
        i += 1; j = 0
    if i >= n:
        return 0 if k == 0 else -987654231

    ret = dp[i][j][k][f]
    if ret != -1:
        return ret

    ret = solve(i,j+1,k,f>>1)
    if not f & 1:
        nf = f | 1<<m
        if j != m-1:
            nf |= 1<<1        
        ret = max(ret, solve(i,j+1,k-1,nf>>1) + arr[i][j])
    dp[i][j][k][f] = ret
    return ret       
    
n,m,k = map(int, input().split())
arr = [[*map(int, input().split())] for i in range(n)]

dp = [[[[-1]*2048 for _ in range(k+1)] for _ in range(m)] for _ in range(n)]
print(solve(0,0,k,0))