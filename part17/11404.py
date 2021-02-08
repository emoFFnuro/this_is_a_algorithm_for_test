import sys
input = sys.stdin.readline
V = int(input())
E = int(input())
INF = sys.maxsize

graph = [[INF] * (V+1) for _ in range(V+1)]


for _ in range(E):
    a , b , c = map(int,input().split())
    if graph[a][b] > c :
        graph[a][b] = c


for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            if i != j and graph[i][j] > graph[i][k] + graph[k][j]:
                graph[i][j] = graph[i][k] + graph[k][j]


for i in range(1,V+1):
    for j in range(1,V+1):
        if graph[i][j] == INF:
            print(0 , end=' ')
        else:
            print(graph[i][j] , end=' ')
    print()

    
