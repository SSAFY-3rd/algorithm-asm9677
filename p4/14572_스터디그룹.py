import sys
input = sys.stdin.readline

def solve():
    N,K,D = map(int, input().split())
    student = []
    for i in range(N):
        M,d = map(int, input().split())
        a = [*map(int, input().split())]
        student.append((d, a))
    student.sort()

    visited = [0]*(K+1)    
    l,r = 0,0
    res = 0

    while r < N:
        if student[l][0] + D >= student[r][0]:
            for x in student[r][1]:
                visited[x] += 1
            r += 1
        else:
            for x in student[l][1]:
                visited[x] -= 1
            l += 1
        total,know = 0,0
        for i in range(1,K+1):
            if visited[i]:
                total += 1
                if visited[i] == (r-l):
                    know += 1
        res = max(res, (total - know) * (r-l))
    print(res)
solve()