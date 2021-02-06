import sys
input = sys.stdin.readline

def solve():
    N = int(input())
    last = -10**9
    res = 0
    for s,e in sorted([*map(int, input().split())] for i in range(N)):
        if last < s: last = s
        if last < e:
            res += e - last
            last = e
    return res
print(solve())