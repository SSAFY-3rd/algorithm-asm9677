import sys
input = sys.stdin.readline

def solve():
    m,n = map(int, input().split())
    arr = [*sorted(int(input()) for i in range(n))][::-1]

    x,y = arr[0],1
    for i in range(1,n):
        if (x-arr[i]) * i > m: break
        m -= (x-arr[i]) * i
        x,y = arr[i],i+1

    if m >= y:
        x,m = x - m//y, m%y
    print((((x-1)**2 * m) + ((x**2) * (y-m)) + sum(arr[i]**2 for i in range(y,n))) % 2**64 if x != 0 else 0)
solve()