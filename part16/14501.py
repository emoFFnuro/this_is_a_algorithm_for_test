## BOJ.14501 -> https://www.acmicpc.net/problem/14501
n = int(input())
T,P = [0 for i in range(n+1)] , [0 for i in range(n+1)]
dp = [0 for i in range(n+1)]

for i in range(n):
    ta , tb = map(int,input().split())
    T[i] = ta
    P[i] = tb

## to compare wage , need to be descending

## we can counsult n , n-1 day  , so we use len(T)
for i in range(len(T)-2, -1 ,-1):
    if T[i] + i <= n:
        dp[i] = max(P[i] + dp[i+T[i]] , dp[i+1])
    else:
        dp[i] = dp[i+1]

print(dp[0])
