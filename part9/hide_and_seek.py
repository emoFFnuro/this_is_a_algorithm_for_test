import sys,heapq

input = sys.stdin.readline
INF = sys.maxsize

## just use dijkstra... so ez

V,E = map(int , input().split())
graph = [[] for _ in range(V+1)]
distance = [INF] * (V+1)

for _ in range(E):
    a , b = map(int,input().split())
    graph[a].append([b,1])
    graph[b].append([a,1])

def dijkstra(start):
    q = []
    heapq.heappush(q,[0 , start])
    distance[start] = 0

    while q:
        dist , now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for idx in graph[now]:
            cost = dist + idx[1]
            if cost < distance[idx[0]]:
                distance[idx[0]] = cost
                heapq.heappush(q , [cost , idx[0]])
    
        
dijkstra(1)
ans_node , ans_distance = 0 , 0
result = []

for i in range(1 , V+1):
    if distance[i] == INF:
        distance[i] = 0

for i in range(1, V+1):
    if ans_distance < distance[i]:
        ans_node = i
        ans_distance = distance[i]
        result = [ans_node]
    elif ans_distance == distance[i]:
        result.append(i)

print(ans_node , ans_distance , len(result))
