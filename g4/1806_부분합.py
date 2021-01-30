import sys
input = sys.stdin.readline

n,k = map(int,input().split())
arr = [*map(int,input().split())]
res = 1<<30

i,j = 0,1
sum = arr[0]
while i < j:
    if sum < k:
        if j == n:
            break
        sum,j = sum+arr[j], j+1
    else:
        res = min(res, j-i)
        sum,i = sum-arr[i], i+1
print(res if res != 1<<30 else 0)