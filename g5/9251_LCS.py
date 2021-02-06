a=' '+input()
b=' '+input()

if len(a) > len(b):
    a,b=b,a

dp=[0]*(len(b)+1)

for i in range(1,len(a)):
    for j in range(len(b)-1,0,-1):
        if a[i]==b[j]:            
            dp[j]=1+dp[j-1]
    for j in range(len(b)):
        if dp[j-1]>dp[j]:
            dp[j]=dp[j-1]
print(max(dp))