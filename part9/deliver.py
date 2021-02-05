import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

V , E , start_node = map(int , input().split())
graph = [[] for i in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    x , y , z = map(int,input().split())
    graph[x].append([y,z])

def dijkstra(start):
    q = []
    heapq.heappush(q , [0,start])
    distance[start] = 0
    
    while q:
        dist , now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q , [cost , i[0]])

dijkstra(start_node)
count = 0
max_distance = 0
for d in distance:
    if d != INF:
        count += 1
        max_distance = max(max_distance , d)

print(count -1 , max_distance)