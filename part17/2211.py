import sys , heapq

input = sys.stdin.readline

N,M = map(int,input().split())
INF = sys.maxsize
graph = [[] for _ in range(N+1)]
distance = [INF] * (N+1)
trace = [0] * (N+1)

for _ in range(M):
    a , b , c = map(int,input().split())
    graph[a].append([b,c])
    graph[b].append([a,c])

def dijkstra(start_node):
    distance[start_node] = 0
    q = list()
    heapq.heappush(q , [0 , start_node])

    while q:
        dist , now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for idx in graph[now]:
            cost = dist + idx[1] 
            if cost < distance[idx[0]]:
                distance[idx[0]] = cost
                heapq.heappush(q , [cost , idx[0]])
                trace[idx[0]]=now

dijkstra(1)
print(sum(1 for i in range(2,N+1) if distance[i] != INF))
for i in range(2,N+1):
    print(i , trace[i])
            






