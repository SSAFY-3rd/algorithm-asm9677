import sys
input = sys.stdin.readline
s = [*map(int, ' '.join(input().replace('6','1').replace('7','2')).split())]
k = int(input())
n = 2**sum(1<=i<=2 for i in s)
if n < k:print(-1)
else:
    k-=1;j = 0
    for i in range(len(s)-1,-1,-1):
        if 1<=s[i]<=2:
            if k & 1<<j:s[i] += 5
            j+=1
    print(*s, sep='')