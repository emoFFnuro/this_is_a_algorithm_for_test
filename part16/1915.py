## BOJ.1915 -> https://www.acmicpc.net/problem/1915

## use rightside-bottom point
##  when i-1,j-1 , i-1,j , i,j-1 is 1 include i,j add 1 to i,j
##      use this routine whole 2d-array

n, m = map(int, input().split()) 
table = [list(map(int, list(input().rstrip()))) for _ in range(n)] 
ans = 0 

for i in range(n): 
    for j in range(m): 
        if i>0 and j>0 and table[i][j] == 1: 
            table[i][j] += min(table[i-1][j], table[i][j-1], table[i-1][j-1]) 
        ans = max(ans, table[i][j]) 

print(ans*ans)

