import sys

input = sys.stdin.readline

N , C = map(int,input().split())
K = int(input())
box = [list(map(int ,input().split())) for _ in range(K)]

box.sort(key=lambda x : x[1])
ans = 0
last = [C] * (N+1)

## use greedy algorithm
##  just renew maximum acceptance number by town number

for i in range(K):
    tmp = C
    print(last , ans)
    for j in range(box[i][0] , box[i][1]):
        tmp = min(tmp , last[j])
    tmp = min(tmp , box[i][2])
    for j in range(box[i][0] , box[i][1]):
        last[j] -= tmp
    ans += tmp

print(ans)