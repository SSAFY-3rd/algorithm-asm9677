import sys
input = sys.stdin.readline

def getRatio():
    ratio = [
        [
            [0,0,0.02,0,0],
            [0,0.10,0.07,0.01,0],
            [0.05,0,0,0,0],
            [0,0.10,0.07,0.01,0],
            [0,0,0.02,0,0],
        ]
    ]   
    
    for d in range(1,4):
        ratio += [[[0]*5 for i in range(5)]]
        for i in range(5):
            for j in range(5):
                ratio[d][i][j] = ratio[d-1][j][4-i]
    return ratio

def move(r,c,d):
    if c < 0: return
    nr,nc = r+dir[d][0], c+dir[d][1]

    tot = 0
    for i in range(5):
        for j in range(5):
            if ratio[d][i][j]:
                x = int(arr[r][c] * ratio[d][i][j])
                tot += x
                arr[r+i-2][c+j-2] += x
    arr[nr][nc] += arr[r][c] - tot
    arr[r][c] = 0

dir = [[0,-1],[1,0],[0,1],[-1,0]]
n = int(input())
ratio = getRatio()
arr = [[*map(int,input().split())] + [0]*5 for i in range(n)] + [[0]*(n+5) for i in range(5)]
    
i = j = n // 2
d,k = 0,1
while True:
    for _ in range(k):
        i,j = i+dir[d][0], j+dir[d][1]
        move(i,j,d)
    if j < 0: break
    if d % 2: k += 1
    d = (d+1) % 4
print(sum(arr[i][j] for j in range(len(arr[i])) for i in range(len(arr)) if not (0 <= i < n and 0 <= j < n)))