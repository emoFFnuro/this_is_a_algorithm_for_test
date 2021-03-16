import sys
import itertools
import copy

dx = [0,0,-1,1]
dy = [-1,1,0,0]

input = sys.stdin.readline

n = int(input())
board = [list(map(str , input().split())) for _ in range(n)]

emptys , teachers , students = list() , list() , list()

for i in range(n):
    for j in range(n):
        if board[i][j] == 'X':
            emptys.append([i,j])
        elif board[i][j] == 'S':
            students.append([i,j])
        elif board[i][j] == 'T':
            teachers.append([i,j])
    
def DFS(board , x , y, idx):
    if x < 0 or x >= n or y < 0 or y >= n or board[x][y] == 'O':
        return
    else:
        board[x][y] = 'T'
        DFS(board , x+dx[idx] , y+dy[idx] , idx)

def check():
    copy_board = copy.deepcopy(board)
    for [x, y] in teachers:
        for i in range(4):
            DFS(copy_board, x, y, i)
    for [x, y] in students:
        if copy_board[x][y] != 'S':
            return False
    return True

for case in list(itertools.combinations(emptys, 3)):
    for [x, y] in case:
        board[x][y] = 'O'
    if check():
        print("YES")
        exit()
    for [x, y] in case:
        board[x][y] = 'X'

print("NO")