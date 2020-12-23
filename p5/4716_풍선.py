import sys
input = sys.stdin.readline

while True:
    n,a,b = map(int, input().split())
    if n == 0: break
    arr = []
    for i in range(n):
        k,x,y = map(int, input().split())
        arr.append((-abs(x-y),x,y,k))
    arr.sort()

    res = 0
    for cha,x,y,k in arr:
        if x < y: 
            if x < k:
                res += x * a + y * (k-x)
                a,b = 0,b-(k-a)
            else:
                res += x * k
                a -= k
        else:
            if b < k:
                res += y * b + x * (k-b)
                a,b = a-(k-b), 0
            else:
                res += y * k
                b -= k
    print(res)