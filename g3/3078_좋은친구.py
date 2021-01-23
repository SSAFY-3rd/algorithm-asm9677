import sys
input = sys.stdin.readline

n,k = map(int, input().split())
names = [0]*(n+k)

for i in range(n):
    names[i] = len(input())-1

res = 0    
count = [0]*21

l,r = -k,-1
while l+1 < n:        
    count[names[l]] -= 1
    res += count[names[l]]
    
    l,r = l+1,r+1
    count[names[r]] += 1
print(res)      
