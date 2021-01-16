def solve(i,j):
    if i == j:
        return 0
    if dp[i][j] != -1:
        return dp[i][j]    
    dp[i][j] = min(solve(i,k) + solve(k+1,j) + matrix[i][0] * matrix[k][1] * matrix[j][1] for k in range(i,j))
    return dp[i][j]

n = int(input())
matrix = [[*map(int, input().split())] for i in range(n)]
dp = [[-1]*n for i in range(n)]
print(solve(0,n-1))