def dfs(s,i):   
    if s == i and visited[i]:
        return [i]
    if visited[i]:
        return []
    visited[i] = True
    return [i] + dfs(s,arr[i]) 

n=int(input())
arr = [0]+[int(input()) for i in range(n)]
visited,res = [],[]
for i in range(1,n+1):
    visited = [0]*(n+1)    
    nums = dfs(i,i)
    if nums[0] == nums[-1]:
        for num in nums:
            res += [num]

res = set(res)
print(len(res))
for num in sorted(res):
    print(num)