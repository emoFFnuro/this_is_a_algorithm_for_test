import sys
from collections import deque
input =  sys.stdin.readline
n = int(input())
arr = list(map(int ,input().split()))
dp = [1 for i in range(n+1)]

for i in range(n):
    for j in range(i):
        if arr[i] > arr[j]:
                dp[i] = max(dp[j] + 1 ,dp[i])

idx = dp.index(max(dp))
maxVal = dp[idx]
dq = deque()

for i in range(n , -1 ,-1):
    if maxVal == dp[i]:
        maxVal -= 1
        dq.appendleft(arr[i])

print(dq)

print(max(dp))
print(' '.join(map(str , dq)))
