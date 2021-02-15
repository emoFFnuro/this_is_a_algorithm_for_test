import sys

input = sys.stdin.readline

r , c = map(int , input().split())
boards = list()

dx = [-1 , 1 , 0 , 0]
dy = [0 , 0 , -1 , 1]

for _ in range(r):
    boards.append(list(map(str , input().strip())))

char_check , ans = [0]*26 ,0

def dfs(x , y , cnt):
    global ans
    if cnt == 26:
        ans = 26
        return
    else:
        ans = max(cnt , ans)
    for idx in range(4):
        nx = x + dx[idx]
        ny = y + dy[idx]
        if 0 <= nx < r and 0 <= ny < c:
            tmp_num = ord(boards[nx][ny]) - ord('A')
            if char_check[tmp_num] == 0:
                char_check[tmp_num] = 1
                dfs(nx,ny,cnt+1)
                char_check[tmp_num] = 0

char_check[ord(boards[0][0]) - ord('A')] = 1
dfs(0,0,1)
print(ans)
