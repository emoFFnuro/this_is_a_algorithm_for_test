n = int(input())
arr = list(map(int, input().split()))

dp = [0] * 100

dp[0] = arr[0]
dp[1] = max(arr[1] , arr[0])

for i in range(2 , n):
    dp[i] = max(dp[i-1] , dp[i-2]+arr[i])

print(dp[n-1])
