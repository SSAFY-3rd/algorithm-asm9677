import sys
sys.setrecursionlimit(10**6)

def solve(i):
    if i == n:
        return 0
    if dp[i] != -1:
        return dp[i]
    mx = mn = arr[i]
    for j in range(i,n):
        mx,mn = max(mx,arr[j]), min(mn,arr[j])
        dp[i] = max(dp[i], solve(j+1) + mx-mn)
    return dp[i]    

n = int(input())
arr,dp = [*map(int, input().split())],[-1]*n
print(solve(0))