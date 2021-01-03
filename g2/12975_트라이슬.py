def solve(i,x,y,z):
    if i == n:
        return x+y+z
    
    x,y,z = sorted([x,y,z])    
    if dp[i][x][y] != -1:
        return dp[i][x][y]

    dp[i][x][y] = max(solve(i+1, x^a[i], y,z), solve(i+1, x, y^a[i],z), solve(i+1, x,y,z^a[i]))
    return dp[i][x][y]

n = int(input())
a = [*map(int, input().split())]
dp = [[[-1]*256 for i in range(256)] for j in range(n)]
print(solve(0,0,0,0))