from math import log2
INF = 1<<31

asd = 0
def solve(l,w,h):   
    l,w,h = sorted([l,w,h])
    
    if l == 0: return 0    
    k = int(log2(l))
    cnt = 0
    for i in range(k,-1,-1):
        cnt += (8**i) * arr[i]

    if cnt < 8**k: 
        return -INF
    x = 2**k
    y = min(cnt//(8**k), h//(2**k))
    
    cnt = (8**k)*y    
    total = 0
    while cnt > 0:        
        mn = min(arr[k], cnt//(8**k))
        cnt -= (8**k)*mn
        arr[k] -= mn
        total += mn
        k-=1
    return solve(l,w,h-(x*y)) + solve(l-x,w,x*y) + solve(x,w-x,x*y) + total

l,w,h = map(int, input().split())
n = int(input())
arr = [0]*20

for i in range(n):
    a,b = map(int,input().split())
    arr[a] = b

res = solve(l,w,h)
print(-1 if res < 0 else res)