import sys
from collections import deque
input = sys.stdin.readline

dx , dy =  [-1,1,0,0], [0,0,-1,1]

r , c = map(int , input().split())
graph = list()
left_cheese = 0
for _ in range(r):
    graph.append(list(map(int,input().split())))
for i in range(r):
    for j in range(c):
        if graph[i][j] == 1:
            left_cheese += 1
def bfs(start_node , left_cheese):
    q = deque()
    q.appendleft(start_node)
    visited[start_node[0]][start_node[1]] = 1
    while q:
        x , y = q.popleft()
        for idx in range(4):
            nx = x + dx[idx]
            ny = y + dy[idx]

            if 0 <= nx < r and 0 <= ny < c and visited[nx][ny] == 0:
                visited[nx][ny] = 1

                if graph[nx][ny] == 1:
                    graph[nx][ny] = 2
                    left_cheese -= 1
                else:
                    q.append([nx,ny])
    return left_cheese

def ridOfCheese():
    for i in range(r):
        for j in range(c):
            if graph[i][j] == 2:
                graph[i][j] = 0

ans = left_cheese
cnt = 0
while left_cheese != 0:
    visited = [[0] * c for _ in range(r)]
    left_cheese = bfs([0,0],left_cheese)

    if left_cheese != 0:
        ans = left_cheese
    
    cnt += 1
    ridOfCheese()
print(cnt)
print(ans)


