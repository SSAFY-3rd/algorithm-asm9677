dir = [[-1,0],[-1,1],[0,1],[1,1],[1,0],[1,-1],[0,-1],[-1,-1]]
n,m,k = map(int, input().split()) 
infos = {}

for i in range(m):
    r,c,m,s,d = map(int, input().split())
    infos[r,c] = [m,s,[d],0]

for _ in range(k):
    new_infos = {}
    for r,c in infos:
        info = infos[r,c]
        for d in infos[r,c][2]:
            m,s = info[0], info[1]
            nr,nc = (r + dir[d][0] * s) % n , (c + dir[d][1] * s) % n
            if nr <= 0: nr += n
            if nc <= 0: nc += n
            
            if not (nr,nc) in new_infos:
                new_infos[nr,nc] = [0,0,[],0]

            new_infos[nr,nc][0] += m
            new_infos[nr,nc][1] += s
            new_infos[nr,nc][2] += [d]         
            new_infos[nr,nc][3] += d % 2

    infos = {} 
    for r,c in new_infos:
        info = new_infos[r,c]
        if len(info[2]) >= 2:
            if info[0] < 5:                
                continue
            l = len(info[2])                
            info[0] //= 5
            info[1] //= l
            if info[3] == l or info[3] == 0:
                info[2] = [*range(0,8,2)]
            else:
                info[2] = [*range(1,8,2)]        
        info[3] = 0
        infos[r,c] = info

print(sum(info[0] * len(info[2]) for info in infos.values()))