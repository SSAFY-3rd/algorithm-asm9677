def solve(i,j,k):
    if j == m:
        i,j = i+1,0
    if i == n:
        return 0
    
    ref = dp[i][j][k]
    if ref != -1:
        return ref

    if k & 1:
        ref = solve(i,j+1,k>>1)
    else:
        num = ''
        f = k
        for jj in range(j,m):
            if k & 1<<(jj-j): break
            num += arr[i][jj]
            f |= 1<<(jj-j)
            ref = max(ref, solve(i,j+1,f>>1) + int(num))
        
        num = ''
        f = k
        for ii in range(i,n):
            num += arr[ii][j]
            f |= (1<<((ii-i)*m))
            ref = max(ref, solve(i,j+1,f>>1) + int(num))        

    dp[i][j][k] = ref
    return ref
    
n,m = map(int, input().split())
arr = [' '.join(input()).split() for i in range(n)]
k = max(1<<m, 2**((n-1)*m+1))

dp = [[[-1]*k for _ in range(m)] for _ in range(n)]
print(solve(0,0,0))