import sys
from collections import deque
import bisect

input = sys.stdin.readline
M , N , L = map(int , input().split())
M_list = list(map(int , input().split()))
M_list.sort()
N_list = deque()
for _ in range(N):
    t_list = list(map(int,input().split()))
    N_list.append(t_list)

cnt = 0
after_sort = list()
## sort it by animal x accor
for animal in N_list:
    after_sort.append(bisect.bisect(M_list , animal[0]))


for i in range(N):
    if (after_sort[i] < M and M_list[after_sort[i]] - N_list[i][0] + N_list[i][1] <= L) or (0 < after_sort[i] and N_list[i][0] + N_list[i][1] - M_list[after_sort[i] - 1]<= L):
        cnt+=1

print(cnt)

