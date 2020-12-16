from collections import deque
import sys
input = sys.stdin.readline

m,n = map(int, input().split())
k = int(input())

route = [[0,0,0,0,0] for i in range(k+2)]
adj = [[] for i in range(k+2)]

for i in range(k):
    b,x1,y1,x2,y2 = map(int, input().split())
    if x1 > x2: x1,x2 = x2,x1
    if y1 > y2: y1,y2 = y2,y1
    route[b] = [x1,y1,x2,y2,x1 == x2]

sx,sy,ex,ey = map(int, input().split())
route[0] = [sx,sy,sx,sy,0]
route[k+1] = [ex,ey,ex,ey,0]

for i in range(k+2):
    ax1,ay1,ax2,ay2,aDir = route[i]
    for j in range(i+1, k+2):
        bx1,by1,bx2,by2,bDir = route[j]

        f = False
        if aDir == bDir == 0:            
            if ay1 == by1 and (ax1 <= bx1 <= ax2 or bx1 <= ax1 <= bx2):
                f = True
        elif aDir == bDir == 1:
            if ax1 == bx1 and (ay1 <= by1 <= ay2 or by1 <= ay1 <= by2):            
                f = True
        else:
            if aDir == 0: 
                if ax1 <= bx1 <= ax2 and by1 <= ay1 <= by2:
                    f = True
            else:
                if bx1 <= ax1 <= bx2 and ay1 <= by1 <= ay2:
                    f = True
        if f: 
            adj[i].append(j)
            adj[j].append(i)

que = deque([0])

res,cnt = -1,0
visited = [0]*(k+2)
visited[0] = 1
while res == -1:
    for _ in range(len(que)):
        cur = que.popleft()
        if cur == k+1:
            res = cnt
            break

        for next in adj[cur]:
            if not visited[next]:
                visited[next] = 1
                que.append(next)
    cnt += 1
print(res - 1)         