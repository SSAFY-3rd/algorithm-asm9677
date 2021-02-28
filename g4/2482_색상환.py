n,k=int(input()),int(input())
dp = [1]*n

for i in range(2, k+1): 
    dp[0] = sum(dp[2:n-1])
    for j in range(1,n-(i*2)+1):
        dp[j] = (dp[j-1] - dp[j+1])
    dp[n-(i*2)+1:] = [0]
if k == 1:
    print(n)
else:
    print((dp[0] + sum(dp)) % 1000000003)