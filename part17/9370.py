import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

def dijkstra(start):
    q = []
    heapq.heappush(q , [0,start])
    distance = [INF] * (n+1)
    distance[start] = 0
    while q:
        dist , now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q , (cost , i[0]))
    
    return distance

tc = int(input())
for _ in range(tc):
    n , m , t = map(int , input().split())
    s , g , h = map(int , input().split())
    distance = [INF] * (n+1)
    graph = [[] for i in range(n+1)]
    destinations = list()

    for idx in range(m):
        a , b , c = map(int , input().split())
        graph[a].append([b,c])
        graph[b].append([a,c])

    for idx in range(t):
        destinations.append(int(input()))

    full_distance = dijkstra(s)
    distance_1 = dijkstra(g)
    distance_2 = dijkstra(h)
    ans = list()

    for dest in destinations:
        if full_distance[g] + distance_1[h] + distance_2[dest] == full_distance[dest] or full_distance[h] + distance_2[g] + distance_1[dest] == full_distance[dest]:
            ans.append(dest)

    ans.sort()

    for _ in ans:
        print(_ , end =' ')
    print()


