import sys
from copy import deepcopy
input = sys.stdin.readline

r , c , t = map(int,input().split())
dust_list = list()
aircleaner_pos = list()
dx = [1,-1,0,0]
dy = [0,0,-1,1]
for i in range(r):
    tmp = list(map(int,input().split()))
    dust_list.append(tmp)
    for j in range(c):
        if tmp[j] == -1:
            aircleaner_pos.append([i,j])

top_pos1 , top_pos2 = aircleaner_pos[0][0] , aircleaner_pos[0][1]
bottom_pos1 , bottom_pos2 = aircleaner_pos[1][0] , aircleaner_pos[1][1]

def diffusion():
    tmp = [[0] * c for i in range(r)]
    tmp[top_pos1][top_pos2] = -1
    tmp[bottom_pos1][bottom_pos2] = -1
    for i in range(r):
        for j in range(c):
            if dust_list[i][j] > 0 :
                cnt = 0
                for k in range(4):
                    x = i + dx[k]
                    y = j + dy[k]
                    if 0 <= x < r and 0 <= y < c and dust_list[x][y] != -1:
                        tmp[x][y] += dust_list[i][j] // 5
                        cnt += 1
                tmp[i][j] += dust_list[i][j] - (dust_list[i][j] // 5 * cnt)
    return tmp

def cleaning(x , y , dir):
    tmp = deepcopy(dust_list)
    tx , ty = x , y - 1
    dust_list[x][y] = 0
    for i in range(4):
        
        while True:
            nx = x + dx[dir[i]]
            ny = y + dy[dir[i]]
            if nx == tx and ny == ty:
                return
            if 0 <= nx <r and 0 <= ny < c:
                dust_list[nx][ny] = tmp[x][y]
            else:
                break
            x , y = nx , ny

## for input test
"""
print(r,c,t)
print(dust_list)
"""
res = 0

for i in range(t):
    dust_list = diffusion()
    cleaning(top_pos1 , top_pos2+1 , [3,1,2,0])
    cleaning(bottom_pos1 , bottom_pos2+1, [3,0,2,1])

dust_list[top_pos1][top_pos2]  , dust_list[bottom_pos1][bottom_pos2] = 0 , 0

for i in range(r):
    res += sum(dust_list[i])    
print(res)