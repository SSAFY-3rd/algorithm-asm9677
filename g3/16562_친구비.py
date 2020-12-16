import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(node):
    if union[node] == node:
        return node
    union[node] = find(union[node])
    return union[node]

n,m,k = map(int, input().split())

pay = [0]+[*map(int, input().split())]
union = [i for i in range(n+1)]
mPay = pay.copy()

for _ in range(m):
    a,b = map(int, input().split())
    a,b = find(a), find(b)
    union[a] = b

for i in range(1,n+1):
    mPay[find(i)] = min(mPay[find(i)], pay[i])
res = 0
for i in range(1,n+1):
    res += mPay[find(i)]
    mPay[find(i)] = 0
print(res if res <= k else 'Oh no')