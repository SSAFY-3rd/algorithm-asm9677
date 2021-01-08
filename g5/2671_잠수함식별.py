s = input()
n = len(s)
dp = [0]*n + [1]
for i in range(n):
    if dp[i-1] & 1:
        dp[i] |= 2 if s[i] == '0' else 4        
    if dp[i-1] & 2 and s[i] == '1':
        dp[i] |= 1
    if dp[i-1] & 4 and s[i] == '0':
        dp[i] |= 8
    if dp[i-1] & 8 and s[i] == '0':
        dp[i] |= 24      
    if dp[i-1] & 16 and s[i] == '1':
        dp[i] |= 17
print(['NOISE','SUBMARINE'][dp[n-1] & 1])