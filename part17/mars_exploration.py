import sys, heapq

input = sys.stdin.readline

nx = [-1 , 1 , 0 , 0]
ny = [0 , 0 , -1 , 1]
INF = sys.maxsize

for tc in range(int(input())):
    n = int(input())
    graph = list()
    for i in range(n):
        graph.append(list(map(int , input().split())))

    distance = [[INF] * n for _ in range(n)]

    x , y = 0 , 0
    q = [(graph[x][y] , x , y)]
    distance[x][y] = graph[x][y]

    while q:
        dist , x , y = heapq.heappop(q)
        if distance[x][y] < dist:
            continue

        for i in range(4):
            dx = x + nx[i]
            dy = y + ny[i]
            if 0 <= dx < n and 0 <= dy < n:
                cost = dist + graph[dx][dy]
                if cost < distance[dx][dy]:
                    distance[dx][dy] = cost
                    heapq.heappush(q , (cost , dx ,dy))
    
    print(distance[n-1][n-1])
