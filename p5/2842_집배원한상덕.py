import sys
sys.setrecursionlimit(10**4)

dir = [[-1,-1],[-1,0],[-1,1],[0,-1],[0,1],[1,-1],[1,0],[1,1]]

def solve(i,j,l,r):
    global visited
    visited[i][j] = True

    for d in range(8):
        ni,nj = i + dir[d][0], j + dir[d][1]
        if 0 <= ni < n and 0 <= nj < n and not visited[ni][nj] and l <= height[ni][nj] <= r:            
            solve(ni,nj,l,r)


n = int(input())
arr = [input() for i in range(n)]
height = [[*map(int,input().split())] for i in range(n)]

si,sj = 0,0
homeList = []
heightList = []
for i in range(n):
    for j in range(n):
        if arr[i][j] == 'P':
            si,sj = i,j
        elif arr[i][j] == 'K':
            homeList += [(i,j)]
        
        heightList += [height[i][j]]
heightList = [*sorted(set(heightList))]
visited = []
l,r = 0,0
hLen = len(heightList)
res = 1<<30
while l < hLen and r < hLen:
    left,right = heightList[l], heightList[r]
    visited = [[0]*n for i in range(n)]
    
    if left <= height[si][sj] <= right:
        solve(si,sj,left,right)

    flag = False
    for a,b in homeList:
        if not visited[a][b]:
            flag = True
            break

    if flag:
        r += 1
    else:
        res = min(res, heightList[r]-heightList[l])
        l += 1
print(res)