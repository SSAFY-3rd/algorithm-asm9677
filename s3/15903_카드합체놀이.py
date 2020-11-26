from heapq import *

n,m = map(int, input().split())
hq = [*sorted(map(int,input().split()))]

for i in range(m):
    k = heappop(hq) + heappop(hq)
    heappush(hq, k)
    heappush(hq, k)

print(sum(hq))