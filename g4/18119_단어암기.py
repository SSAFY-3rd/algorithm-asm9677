import sys
input = sys.stdin.readline

n,m = map(int, input().split())
words = [[] for i in range(26)]

for i in range(n):
    for ch in set(input().rstrip()):
        words[ord(ch)-97].append(i)

outer = [0]*n
ans = n
for k in range(m):
    o,x = map(ord, input().split())    
    x -= 97

    if o == 49:
        for i in words[x]:
            if outer[i] == 0:
                ans -= 1
            outer[i] += 1
    else:
        for i in words[x]:            
            outer[i] -= 1
            if outer[i] == 0:
                ans += 1    
    print(ans)