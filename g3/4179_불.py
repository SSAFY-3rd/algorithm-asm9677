import queue

dir = [[1,0],[0,1],[-1,0],[0,-1]]

n,m = map(int, input().split())
arr = [input() for i in range(n)]
visited = [[False]*m for i in range(n)]
que = queue.deque()
for i in range(n):
    for j in range(m):
        if arr[i][j] == '.':
            continue        
        elif arr[i][j] == 'J':
            que.append((i,j,1))
        elif arr[i][j] == 'F':
            que.appendleft((i,j,0))
        visited[i][j] = True

res,cnt = -1,0
while que and res == -1:
    for k in range(len(que)):
        i,j,s = que.popleft()
        for d in range(4):
            ni,nj = i+dir[d][0],j+dir[d][1]
            if 0 <= ni < n and 0 <= nj < m and not visited[ni][nj]:                
                visited[ni][nj] = True
                que.append((ni,nj,s))
            elif (ni < 0 or ni >= n or nj < 0 or nj >= m) and s:
                res = cnt + 1
                break
    cnt += 1
print('IMPOSSIBLE' if res == -1 else res)