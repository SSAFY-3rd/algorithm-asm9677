def solve(a,b):
    for i in range(1,61):
        if (2**i-1)%b == 0:
            s = bin((2**i-1)//b*a)[2:].replace('1','*').replace('0','-')
            s = (i-len(s))*'-' + s
            return s
    return -1
a,b=map(int,input().split())
print(solve(a,b))