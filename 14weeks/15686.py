import sys
from collections import deque
from itertools import combinations
input = sys.stdin.readline

n , m = map(int ,input().split())
map_info = list()
for _ in range(n):
    map_info.append(list(map(int ,input().split())))

visited = [[0] * (n) for _ in range(n)]

## for finding chicken franchise
chicken_set = list()
house_set = list()
for i in range(n):
    for j in range(n):
        if map_info[i][j] == 2:
            chicken_set.append([i,j])
        elif map_info[i][j] == 1:
            house_set.append([i,j])

comb_ref_fran = combinations(chicken_set , m)

res = sys.maxsize
for fran in comb_ref_fran:
    ans = 0
    for home in house_set:
        ans += min([abs(home[0]-i[0]) + abs(home[1]-i[1]) for i in fran])
        if res <= ans: break
    if ans < res : res = ans

print(res)
