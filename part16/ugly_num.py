## to make primefactor , multiply 2 , 3 , 5 only and to follow asecending order always find least one

n = int(input())

ugly_dp = [0] * n
ugly_dp[0] = 1


idx_2 = idx_3 = idx_5 = 0

next_2 , next_3 , next_5 = 2 , 3 , 5

for i in range(1,n):
    ugly_dp[i] = min(next_2 , next_3 , next_5)
    print(next_2 , next_3 , next_5 , ugly_dp)

    if ugly_dp[i] == next_2:
        idx_2 += 1
        next_2 = ugly_dp[i] * 2
    if ugly_dp[i] == next_3:
        idx_3 += 1
        next_3 = ugly_dp[i] * 3
    if ugly_dp[i] == next_5:
        idx_5 += 1
        next_5 = ugly_dp[i] * 5
    
