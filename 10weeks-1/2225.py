import sys 

input = sys.stdin.readline

N , K = map(int ,input().split())
dp = [[0] * (N+1) for _ in range(K+1)]
dp[0][0] = 1
for idx in range(1 , K+1):
    for j_idx in range(N+1):
        dp[idx][j_idx] = dp[idx-1][j_idx] + dp[idx][j_idx-1]
        dp[idx][j_idx] %= 1000000000

print(dp[K][N])

