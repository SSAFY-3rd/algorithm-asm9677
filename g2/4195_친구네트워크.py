import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def find(u):
    if parent[u] == u:
        return u
    parent[u] = find(parent[u])
    return parent[u]

def union(u,v):
    pu,pv = find(u), find(v)
    if pu != pv:
        parent[pu] = parent[pv]
        count[pv] += count[pu]    
    return count[pv]

def solve(n):
    global parent,count
    parent,count = [],[]
    number,idx = {},0     

    for _ in range(n):
        s1, s2 = input().split()
        if not s1 in number:
            parent.append(idx)
            count.append(1)
            number[s1] = idx 
            idx += 1
        if not s2 in number:
            parent.append(idx)
            count.append(1)
            number[s2] = idx
            idx += 1
        print(union(number[s1], number[s2]))

for T in range(int(input())):
    solve(int(input()))