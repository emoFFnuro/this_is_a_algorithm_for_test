import sys , heapq

INF = sys.maxsize

n , s , a , b = 6,4,6,2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]

def dijkstra(graph , start_node , n , d , fares):
    q = []
    distance = [INF] * (n+1)
    distance[start_node] = 0
    heapq.heappush(q , (0 , start_node))
    while q:
        dist , now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for idx in graph[now]:
            cost = dist + idx[1]
            if cost < distance[idx[0]]:
                distance[idx[0]] = cost
                heapq.heappush(q ,(cost , idx[0]) )
    
    return distance[d]
def solution(n, s, a, b, fares):
    graph = [[] for _ in range(n+1)]
    for idx in fares:
        graph[idx[0]].append([idx[1] , idx[2]])
        graph[idx[1]].append([idx[0] , idx[2]])
    
    res = dijkstra(graph , s , n, a , fares) + dijkstra(graph, s ,n , b, fares)
    for i in range(1,n+1):
        if s != i:
            res = min(res , dijkstra(graph,s,n,i,fares) + dijkstra(graph,i,n,a,fares) + dijkstra(graph,i,n,b,fares))

    return res
