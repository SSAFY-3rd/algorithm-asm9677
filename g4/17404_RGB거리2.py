import sys
In=sys.stdin.readline

n,k=int(In()),1<<31
r,g,b=map(int,In().split())
if n == 1:
    print(min(r,g,b))
else:
    x,y,z=map(int,In().split())
    dp=[k,r+y,r+z,g+x,k,g+z,b+x,b+y,k]
    for i in range(2,n):
        r,g,b=map(int,In().split())
        for s in range(0,9,3):            
            dp[s:s+3]=[min(dp[s+1],dp[s+2])+r,min(dp[s],dp[s+2])+g,min(dp[s],dp[s+1])+b]
    dp[::4]=[k]*3
    print(min(dp))