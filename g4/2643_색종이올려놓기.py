n = int(input())
dp,a = [1]*n, sorted([*sorted(map(int,input().split()))] for i in range(n))[::-1]
for i in range(n):
    for j in range(i+1, n):
        if a[i][1] >= a[j][1]:
            dp[j] = max(dp[j], dp[i] + 1)
print(max(dp))