from collections import deque
import sys
input = sys.stdin.readline
dir = [[0,1],[1,0],[0,-1],[-1,0]]

def solve():       
    n,k = int(input()),int(input())
    arr = [[0]*n for i in range(n)]
    snake = deque([(0,0)])
    arr[0][0] = 9 
    change = {}

    for _ in range(k):
        r,c = map(int, input().split())
        arr[r-1][c-1] = 1    
    
    for _ in range(int(input())):
        x,c = input().split()
        change[int(x)] = 1 if c == 'D' else -1
    
    t = i = j = d = 0
    while True:   
        if t in change:
            d = (d + change[t]) % 4
        t += 1

        ni,nj = i+dir[d][0], j+dir[d][1]
        if 0 <= ni < n and 0 <= nj < n and arr[ni][nj] != 9:
            if arr[ni][nj] != 1:
                si,sj = snake.popleft()
                arr[si][sj] = 0
            snake.append((ni,nj))
            arr[ni][nj] = 9
        else:
            break
        i,j = ni,nj
    print(t)
solve()