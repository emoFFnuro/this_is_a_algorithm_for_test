import sys
input = sys.stdin.readline

V , E = map(int,input().split())
INF = sys.maxsize
graph = [[INF] * (V+1) for _ in range(V+1)]

for a in range(1, V + 1):
    for b in range(1, V + 1):
        if a == b:
            graph[a][b] = 0


for _ in range(E):
    ta , tb = map(int,input().split())
    graph[ta][tb] = 1
    graph[tb][ta] = 1

x , k = map(int,input().split())

for k in range(1,V+1):
    for i in range(1,V+1):
        for j in range(1,V+1):
            graph[i][j] = min(graph[i][j] , graph[i][k] + graph[k][j])



distance = graph[1][x] + graph[x][k]

if distance >= INF:
    print(-1)
else:
    print(distance)