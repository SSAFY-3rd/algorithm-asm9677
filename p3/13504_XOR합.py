def insert(trie, num):        
    for idx in range(31,0,-1):
        f = num & (1<<idx) != 0
        if not trie[f]:
            trie[f] = [[],[]]    
        trie = trie[f]
    trie[num & 1] = num
    
def query(trie, num):
    for idx in range(31,-1,-1):
        f = num & (1<<idx) == 0 
        trie = trie[f if trie[f] else not f]
    return trie

def solve():
    n = int(input())
    nums = [*map(int, input().split())]

    trie = [[],[]]
    res = total = nums[0]
    for num in nums[1:]:
        insert(trie,total)
        total ^= num
        res = max(res, total ^ query(trie, total), total)
    print(res)

for T in range(int(input())):
    solve()