import sys
input = sys.stdin.readline

n = int(input())
light = [[0]*3010 for i in range(3010)]
dp = [[0]*3010 for i in range(3010)]
left,right = [0]*9010,[0]*9010

for i in range(n):
    x,y = map(int, input().split())
    x,y = x + 1500, y + 1500
    light[y][x] += 1

for i in range(3001):
    for j in range(3001):
        left[j+i] += light[i][j]
        right[j-i] += light[i][j]
    for j in range(i+1):
        dp[i][0] += left[j]
    for j in range(1,3001):
        dp[i][j] = dp[i][j-1] + left[i+j] - right[j-i-1]
for k in range(int(input())):
    x,y = map(int, input().split())
    x,y = x + 1500, y + 1500
    print(dp[y][x])