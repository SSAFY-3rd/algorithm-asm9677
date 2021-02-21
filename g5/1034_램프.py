n,m=map(int,input().split())
arr = [input() for i in range(n)]
k = int(input())
try:print(max(arr.count(arr[i]) for i in range(n) if arr[i].count('0') <= k and arr[i].count('0') % 2 == k % 2))
except:print(0)