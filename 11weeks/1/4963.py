import sys
from collections import deque
input = sys.stdin.readline

dx = [-1,1,0,0,-1,1,-1,1]
dy = [0,0,-1,1,-1,-1,1,1]

def bfs(startnode):
    global count
    q = deque()
    q.append(startnode)
    visited[startnode[0]][startnode[1]] = 1
    graph_info[startnode[0]][startnode[1]] = 0
    while q:
        x , y = q.popleft()
        for i in range(8):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < c and 0 <= ny < r:
                if visited[nx][ny] == 0 and graph_info[nx][ny] == 1:
                    q.append([nx,ny])
                    visited[nx][ny] = 1
                    graph_info[nx][ny] = 0
    count += 1
    

while True:
    r , c = map(int, input().split())
    count = 0
    ## first exit condition
    if r == 0 and c == 0:
        break
    graph_info = list()
    visited = [[0] * r for _ in range(c)]
    for idx in range(c):
        graph_info.append(list(map(int , input().split())))
    for i in range(c):
        for j in range(r):
            if graph_info[i][j] == 1:
                bfs([i,j])
    print(count)