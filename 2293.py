## BOJ.2293 -> https://www.acmicpc.net/problem/2293
## same with kanpsack problem..
import sys
n, k = map(int,sys.stdin.readline().split())

coin = []
for _ in range(n):
    coin.append(int(sys.stdin.readline()))

dp = [0] * (k+1)
dp[0] = 1
for c in coin:
    for i in range(1,k+1):
        if c <= i:
            dp[i] += dp[i-c]

print(dp[k])
