## BOJ 1932 -> https://www.acmicpc.net/problem/1932
n = int(input())
dp = list()

for _ in range(n):
    dp.append(list(map(int , input().split())))

## level can be 500  , so we use dp to solve this problem

## only allowed direction -> left down , down
##  in problem said only diagonally left right but in array , it means left down and down 

## e.g
##  7
##  8 0
##  1 2 3

for i in range(1 , n):
    for j in range(i + 1):
        if j == 0:
            left_down = 0
        else:
            left_down = dp[i-1][j-1]
        
        if j == i:
            up = 0
        else:
            up = dp[i-1][j]
        
        dp[i][j] = dp[i][j] + max(left_down , up)
    
print(max(dp[n-1]))
