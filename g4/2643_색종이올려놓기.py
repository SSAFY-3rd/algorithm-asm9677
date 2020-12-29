import sys
input = sys.stdin.readline

def solve():
    n = int(input())
    dp,arr = [1]*n, []
    for i in range(n):
        a,b = map(int,input().split())
        if a < b: a,b = b,a
        arr.append((a,b))
    arr.sort(reverse=True)

    for i in range(1,n):    
        for j in range(i):
            if arr[i][1] <= arr[j][1]:
                dp[i] = max(dp[i], dp[j] + 1)
    print(max(dp))
solve()