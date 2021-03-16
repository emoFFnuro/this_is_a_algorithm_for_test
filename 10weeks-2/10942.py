import sys

input = sys.stdin.readline

n = int(input())
d = [int(i) for i in input().split()]
dp = [[0] * n for _ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if d[i] == d[i+1]:
        dp[i][i+1] = 1

for i in range(2,n):
    for j in range(n-i):
        if d[j] == d[j+i] and dp[j+1][j+i-1] == 1:
            dp[j][j+i] = 1

tc_n = int(input())
for _ in range(tc_n):
    i , j = [int(a) for a in input().split()]
    print(dp[i-1][j-1])

