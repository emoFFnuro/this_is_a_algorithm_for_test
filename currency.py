N,M = map(int , input().split())
arr = list()
for i in range(N):
    arr.append(int(input()))

dp = [10001] * (M+1)

dp[0] = 0

for i in range(N):
    for j in range(arr[i] , M+1):
        print(i, j ,arr[i], dp)
        if dp[j - arr[i]] != 10001:
            dp[j] = min(dp[j] , dp[j-arr[i]]+1)

