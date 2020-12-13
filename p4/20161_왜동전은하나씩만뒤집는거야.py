def solve(i,f):
    if i + k - 1 == n:        
        return 0 if f == flag else INF
    
    if dp[i][f] != -1:
        return dp[i][f]
    
    dp[i][f] = INF
 
    tmp = 1-src[i] if f & 1 else src[i]
    if tmp == dst[i]:
        dp[i][f] = solve(i+1, f >> 1)    
        dp[i][f] = min(dp[i][f], solve(i+1, (f ^ bit[0]) >> 1) + 1)
        for x in range(k):            
            dp[i][f] = min(dp[i][f], solve(i, f ^ bit[x]) + 1)
    else:   
        dp[i][f] = min(dp[i][f], solve(i, f ^ bit[0]) + 1)    
        for x in range(1,k):            
            dp[i][f] = min(dp[i][f], solve(i+1, (f ^ bit[x]) >> 1) + 1)
            
    return dp[i][f]    

INF = 1<<30
n,k = map(int, input().split())
src,dst = [*map(int, input().split())],[*map(int, input().split())]
bit = [((1<<k) - 1) ^ (1<<i) for i in range(k)]
flag = 0
for i in range(n-1, n-k, -1):
    flag <<= 1
    flag = flag | (src[i] != dst[i])

dp = [[-1]*(1<<k) for i in range(n)]
res = solve(0,0)
print(-1 if res >= INF else res)