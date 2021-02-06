def m(a, b):
    r=[[0 for i in range(len(a))] for j in range(len(a))]   
    l=len(a)
    for i in range(l):
        for j in range(l):
            for k in range(l):
                r[i][j]+=a[i][k] * b[k][j]
            r[i][j]%=1000
    return r
def f(a, n):
    if n==1:return a
    r=f(a,n//2)
    r=m(r, r)
    if n%2:r=m(r, a)
    return r
N,B=map(int,input().split())
a=[]
for i in range(N):
    a+=[list(map(int, input().split()))] 
b=f(a,B)
for i in b:
    for j in i:
        print(j%1000, end=' ')
    print()