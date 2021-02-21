import sys
input=sys.stdin.readline

a=b=c=d=e=f=0
for i in range(int(input())):
    x,y,z=map(int,input().split())
    a,b,c=x+max(a,b),y+max(a,b,c),z+max(b,c)
    d,e,f=x+min(d,e),y+min(d,e,f),z+min(e,f)
    
print(max(a,b,c),min(d,e,f))