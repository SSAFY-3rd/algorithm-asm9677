import sys 
input = sys.stdin.readline

def solve():  
    trie = [{},0,0]
    
    n1 = int(input())
    for i in range(n1):
        s = input().rstrip()
        insert(trie, 1,0,s,0)

    n2 = int(input())
    for i in range(n2):
        s = input().rstrip()
        insert(trie, 0,1,s,0)  
    print(query(trie, 0) + n1 - query(trie, 1))

def insert(node, l,r, s,idx):
    node[1] += l; node[2] += r
    if len(s) == idx:
        return   

    next = s[idx]    
    if not next in node[0]:
        node[0][next] = [{},0,0]

    insert(node[0][next], l,r,s,idx+1)

def query(node, f):
    if node[2] == 0:                
        return node[1] if f else 1
    return sum(query(node[0][next], f) for next in node[0])

for T in range(int(input())):
    solve()