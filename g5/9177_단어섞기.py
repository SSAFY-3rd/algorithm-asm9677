import sys
input = sys.stdin.readline

def solve(i,j,k):    
    if k == n+m: return 1
    if dp[i][j] != -1:
        return dp[i][j]    
    dp[i][j] = (i < n and w1[i] == w3[k] and solve(i+1,j,k+1)) or (j < m and w2[j] == w3[k] and solve(i,j+1,k+1))    
    return dp[i][j]

for i in range(int(input())):
    w1,w2,w3 = input().split()
    n,m = len(w1),len(w2)
    dp = [[-1]*(m+1) for _ in range(n+1)]
    print('Data set {0}: {1}'.format(i+1, ['no','yes'][solve(0,0,0)]))