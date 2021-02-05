import sys

##   basic idea 
##      1. use floyd-warshall algorithm to count higher , lower scored student
##      2. in traversal , count whole student. 
##      3. if that is same with N-1 , he or she can estimate accuretely (his or her) rank

input = sys.stdin.readline
INF = sys.maxsize

N , M = map(int ,input().split())
graph = [[INF] * (N+1) for _ in range(N+1)]

for i in range(1 , N+1):
    for j in range(1 , N+1):
        if i == j:
            graph[i][j] = 0

for _ in range(M):
    a , b = map(int,input().split())
    graph[a][b] = 1

for k in range(1,N+1):
    for i in range(1,N+1):
        for j in range(1,N+1):
            if graph[i][k] + graph[k][j] == 2:
                graph[i][j] = 1

ans = [0] * (N+1)

for row in range(1,N+1):
    for col in range(1,N+1):
        if graph[row][col] == 1:
            ans[row] += 1
            ans[col] += 1

print(ans)
        
