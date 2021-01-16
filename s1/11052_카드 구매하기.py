n=int(input())
a=[*map(int,input().split())]
for i in range(1,n):
    a[i]=max(a[i],max(a[j]+a[i-j-1] for j in range(i)))
print(a[-1])