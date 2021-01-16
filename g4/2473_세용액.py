def solve(n,arr):
    min_val = 10**18
    res = []
    for k in range(n-2):
        base,l,r = arr[k],k+1, n-1
        while l < r:
            tmp = base+arr[l]+arr[r]
            if min_val > abs(tmp):
                min_val,res = abs(tmp),[arr[k], arr[l], arr[r]]    
                if tmp == 0: return res
            if tmp < 0:
                l += 1
            else:
                r -= 1
    return res 
print(*solve(int(input()), [*sorted(map(int, input().split()))]))