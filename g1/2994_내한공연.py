INF = 1<<30
t,n = map(int, input().split())
arr = [0] + [*map(int, input().split())]
res = [0]*(n+1)
dp = [[INF]*(t+1) for i in range(n+1)]
dp[0][0] = 0

for i in range(1,n+1):
    for j in range(t+1):        
        if j >= arr[i]:
            dp[i][j] = dp[i-1][j-arr[i]]        
        if dp[i-1][j] + arr[i] <= t:
            dp[i][j] = min(dp[i][j], dp[i-1][j] + arr[i])

for j in range(t+1):
    if dp[n][j] <= t:
        break

i,j = n,j
left,right = 0,0
while i > 0:
    if j >= arr[i] and dp[i][j] == dp[i-1][j-arr[i]]:
        res[i] = left
        left += arr[i]
        j -= arr[i]
    else:
        res[i] = right
        right += arr[i]
    i -= 1

print(*res[1:])