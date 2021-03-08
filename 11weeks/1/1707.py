import sys
from collections import deque
input = sys.stdin.readline


def bfs(startnode):
    q = deque()
    q.append(startnode)
    visited[startnode] = 1
    while q:
        next_node = q.popleft()
        for node in graph_info[next_node]:
            if visited[node] == 0:
                visited[node] = -visited[next_node]
                q.append(node)
            else:
                if visited[node] == visited[next_node]:
                    return False
    return True
TC = int(input())
while TC > 0:
    V , E = map(int ,input().split())
    isBipartite = True
    graph_info = [[]  for _ in range(V+1)]
    visited = [0] *(V+1)
    for _ in range(E):
        fr , to = map(int , input().split())
        graph_info[fr].append(to)
        graph_info[to].append(fr)
    for idx in range(1 , V+1):
        if visited[idx] == 0:
            if not bfs(idx):
                isBipartite = False
                break
    TC-=1
    print("YES" if isBipartite else "NO")

