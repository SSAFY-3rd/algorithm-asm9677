n,m,s,v = map(int, input().split())
d = s*v

def getDist(p1,p2):
    return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

def match(x):
    visited[x] = True
    for y in adj[x]:        
        if node[y] == -1 or (not visited[node[y]] and match(node[y])):
            node[y] = x
            return True
    return False

mouse_pos = [[*map(float, input().split())] for i in range(n)]
hole_pos = [[*map(float, input().split())] for i in range(m)]

adj = [[] for i in range(n)]
node = [-1]*m
visited = []

for i in range(n):
    for j in range(m):
        if getDist(mouse_pos[i], hole_pos[j]) <= d:
            adj[i] += [j]

res = n
for i in range(n):
    visited = [0]*m
    res -= match(i)
print(res)