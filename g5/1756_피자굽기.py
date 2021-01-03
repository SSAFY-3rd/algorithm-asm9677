import sys
input = sys.stdin.readline

def solve():
    d,n = map(int, input().split())
    arr = [*map(int, input().split())]
    
    for i in range(1, d):    
        arr[i] = arr[i-1] if arr[i-1] < arr[i] else arr[i]
        
    r = d
    for num in map(int, input().split()):
        while True:
            r-=1  
            if r < 0 or arr[r] >= num: break      
        if r == -1: break
    print(r + 1)
solve()