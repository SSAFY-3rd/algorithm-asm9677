from itertools import combinations

def solve(combi):    
    for a,b in combi:     
        if arr[a][b-1] == 1 or arr[a][b+1] == 1:
            return False
        
    ord = [i for i in range(m+1)]
    for i in range(1,n+1):
        for j in range(1,m):
            if arr[i][j]:
                ord[j],ord[j+1] = ord[j+1],ord[j]

    if sum(ord[k] == k for k in range(1,m+1)) == m:
        return True
    return False

m,k,n = map(int, input().split())
arr = [[0]*(m+1) for i in range(n+1)]
res = -1

for _ in range(k):
    a,b = map(int, input().split())
    arr[a][b] = 1

for k in range(4):
    for combi in combinations([[i,j] for j in range(1,m) for i in range(1,n+1)], k):
        flag = False
        for a,b in combi:
            if arr[a][b-1] == 1 or arr[a][b] == 1 or arr[a][b+1] == 1:
                flag = True
                break
        if flag: continue

        for a,b in combi:  
            arr[a][b] = 1

        if solve(combi):
            res = k
            break     

        for a,b in combi:            
            arr[a][b] = 0
    if res != -1: break
print(res)