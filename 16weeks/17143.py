import sys
input = sys.stdin.readline

r,c,m = map(int,input().split())
sea_list = [[0] * c for _ in range(r)]

for i in range(m):
    sr , sc , s,d,z = map(int ,input().split())
    sea_list[sr-1][sc-1] = [s,d-1,z]

## for input test
"""
for i in range(r):
    for j in range(c):
        print(sea_list[i][j] , end = ' ')
    print()
"""
res = 0
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def sharkMovement():
    tmp = [[0] * c for _ in range(r)]
    for i in range(r):
        for j in range(c):
            if sea_list[i][j] != 0:
                x , y , s , d , z = i,j,sea_list[i][j][0] , sea_list[i][j][1] , sea_list[i][j][2]
                while s > 0:
                    x += dx[d]
                    y += dy[d]
                    if 0 <= x < r and 0 <= y < c:
                        s -= 1
                    else:
                        x -= dx[d]
                        y -= dy[d]
                        if d == 0 : d = 1
                        elif d == 1 : d = 0
                        elif d == 2 : d = 3
                        elif d == 3 : d = 2
                if tmp[x][y] == 0:
                    tmp[x][y] = [sea_list[i][j][0] , d , z]
                else:
                    if tmp[x][y][2] < z:
                        tmp[x][y] = [sea_list[i][j][0] , d , z]
    return tmp

for i in range(c):
    for j in range(r):
        if sea_list[j][i] != 0:
            res += sea_list[j][i][2]
            sea_list[j][i] = 0
            break
    sea_list = sharkMovement()

print(res)