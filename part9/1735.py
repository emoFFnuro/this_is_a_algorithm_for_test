## BOJ 1753
## https://www.acmicpc.net/problem/1753

import sys
import heapq

## input 
input = sys.stdin.readline

N,M = map(int , input().split())
start_node = int(input())
graph = [[] for _ in range(N+1)]
INF = sys.maxsize
distance = [INF] * (N+1)
q = list()

for i in range(M):
    a , b , c = map(int , input().split())
    graph[a].append((b,c))

## for check input
# print(N,M,start_node,graph)
# print(distance,visited)

def dijkstra(start):
    heapq.heappush(q , [0 , start])
    distance[start] = 0

    while q:
        dist , now = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i,j in graph[now]:
            cost = dist + j
            if cost < distance[i]:
                distance[i] = cost
                heapq.heappush(q , [cost , i ])

dijkstra(start_node)

for i in distance[1:]:
    print(i if i != INF else 'INF')
