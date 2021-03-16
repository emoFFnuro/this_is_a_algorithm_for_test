
from bisect import bisect_left

children = []
for _ in range(int(input())):
    children.append(int(input()))

dp = []
for i in children:
    k = bisect_left(dp , i)

    if len(dp) <= k:
        dp.append(i)
    else:
        dp[k] = i
    
