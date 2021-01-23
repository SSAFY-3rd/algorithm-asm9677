import sys
input = sys.stdin.readline

def insert(trie, s, idx):
    if idx < 0:
        return 
    child = {} if not s[idx] in trie else trie[s[idx]]
    insert(child, s, idx-1)
    trie[s[idx]] = child

def pre_order(trie, cnt):
    for key in sorted(trie.keys()):
        print('-'*cnt + key)
        pre_order(trie[key], cnt+2)

trie = {}
n = int(input())
for _ in range(n):
    s = input().split()[:0:-1]
    insert(trie, s, len(s)-1)
pre_order(trie,0) 