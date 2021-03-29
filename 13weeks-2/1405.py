import sys

N , pe , pw , ps , pn = map(int,input().split())
p = [pe/100 , pw /100 , ps/100 , pn/100]
dx , dy = [-1,1,0,0] , [0,0,-1,1]
cnt = 0

def dfs(i,j,k,probability,visited):
    global cnt
    if k==N:
        if len(set(visited)) == N+1:
            cnt += probability
        return
    
    for idx in range(4):
        nx , ny = i+dx[idx] , j+dy[idx]
        if (nx,ny) not in visited:
            visited.append((nx,ny))
            dfs(i+dx[idx] , j + dy[idx] , k+1 , probability*p[idx] , visited)
            visited.pop()

dfs(0,0,0,1,[(0,0)])
print('{:.10f}'.format(cnt))