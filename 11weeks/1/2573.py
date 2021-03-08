import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**4)

dx , dy = [-1,1,0,0] , [0,0,-1,1]
r , c = map(int,input().split())
graph = list()
graph_minus = [[0] * c for _ in range(r)]
visited = list()
for _ in range(r):
    graph.append(list(map(int , input().split())))


def dfs(node):
    visited[node[0]][node[1]] = 1
    x , y = node[0] , node[1]
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]

        if 0 <= nx < r and 0 <= ny < c:
            if not visited[nx][ny] and graph[nx][ny] > 0:
                dfs([nx,ny])

def getAdjacency(x , y):
    cnt = 0
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
    
        if 0 <= nx < r and 0 <= ny < c:
            if graph[nx][ny] <= 0 and graph[x][y] > 0:
                cnt += 1
    
    return cnt

def getGlacier():
    cnt = 0
    for i in range(r):
        for j in range(c):
            if graph[i][j] > 0 and not visited[i][j]:
                dfs([i,j])
                cnt += 1
    
    return cnt

tmp_glacier = 0
cnt = 0
while True:
    visited = [[0] * c for _ in range(r)]
    tmp_glacier = getGlacier()
    if tmp_glacier == 0:
        print(0)
        break
    elif tmp_glacier >= 2:
        print(cnt)
        break
    else:
        cnt += 1
        for i in range(r):
            for j in range(c):
                if graph[i][j] > 0:
                    graph_minus[i][j] = getAdjacency(i,j)
        
        for i in range(r):
            for j in range(c):
                graph[i][j] -= graph_minus[i][j]

    
    

    



                
    