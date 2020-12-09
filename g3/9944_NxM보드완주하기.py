import sys
sys.setrecursionlimit(10**4)
INF = 10**9

def solve(i,j,d,k):
    if k == 0:
        return 0
    
    res = INF    
    ni,nj = i,j
    while 0 <= ni < n and 0 <= nj < m and arr[ni][nj] == '.':
        arr[ni][nj] = '*'
        k -= 1
        ni,nj = ni + dir[d][0], nj + dir[d][1]
    ni,nj = ni - dir[d][0], nj - dir[d][1]

    isComplete = k == 0

    for nd in range(4):
        nni,nnj = ni + dir[nd][0], nj + dir[nd][1]
        if 0 <= nni < n and 0 <= nnj < m and arr[nni][nnj] == '.':
            res = min(res, solve(nni,nnj,nd, k) + 1)
 
    ni,nj = ni + dir[d][0], nj + dir[d][1]
    while ni != i or nj != j:        
        ni,nj = ni - dir[d][0], nj - dir[d][1]
        arr[ni][nj] = '.'
        k += 1    

    return 1 if isComplete else res

dir = [[1,0],[0,1],[-1,0],[0,-1]]
testCase = 1

while True:
    try:
        n,m = map(int, input().split())
        arr = [' '.join(input()).split() for i in range(n)]

        k = sum(1 for j in range(m) for i in range(n) if arr[i][j] == '.')
        res = 0
        if k != 1:            
            res = INF
            for i in range(n):
                for j in range(m):
                    if arr[i][j] == '.':
                        for d in range(4):                                
                            res = min(res, solve(i,j,d,k))
        print('Case %d: %d' %(testCase, res if res < INF else -1))
        testCase += 1
    except: break