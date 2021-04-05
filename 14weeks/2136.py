import sys
input = sys.stdin.readline

N , L =  map(int , input().split())
ant_list_origin = list()

for _ in range(N):
    ant_list_origin.append(int(input()))

ant_list = sorted(ant_list_origin , key=abs)
print(ant_list)

lt , rt = 0 , 0
for i in range(N):
    if ant_list[i] > 0:
        lt = L - ant_list[i]
        lidx = i
        break
for i in range(N-1 ,-1 ,-1):
    if ant_list[i] < 0:
        rt = ant_list[i] * (-1)
        ridx = i
        break

RightSide , LeftSide = 0 , 0
for i in range(N):
    if ant_list[i]:
        if ant_list[i] > 0:
            RightSide += 1
        else:
            LeftSide += 1

if lt > rt:
    print(ant_list_origin.index(ant_list[LeftSide])+1 , lt)
else:
    print(ant_list_origin.index(ant_list[LeftSide-1])+1 , rt)
