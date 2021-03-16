import sys

s1 = input().strip()
s2 = input().strip()
len_s1 , len_s2 = len(s1) , len(s2)
dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

for idx in range(1,len_s1+1):
    for j_idx in range(1,len_s2+1):
        if s1[idx-1] == s2[j_idx-1]:
            dp[idx][j_idx] = dp[idx-1][j_idx-1] + 1
        else:
            dp[idx][j_idx] = max(dp[idx-1][j_idx] , dp[idx][j_idx-1])

print(dp[-1][-1])