from heapq import *
import sys
input = sys.stdin.readline

N = int(input())     
pos = [*sorted([[*sorted(map(int, input().split()))] for i in range(N)], key=lambda x:x[1])]
d = int(input())
hq,res = [],0

for s,e in pos:
    heappush(hq, s)
    if hq and hq[0] < e - d: heappop(hq)
    res = max(res, len(hq))    
print(res)