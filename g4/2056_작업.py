import sys
input = sys.stdin.readline
n=int(input())
dp=[0]*(n+1)
for i in range(1,n+1):
    nums=[*map(int,input().split())]
    dp[i]=nums[0]
    if nums[1]:
        dp[i]+=max(dp[k] for k in nums[2:])
print(max(dp))