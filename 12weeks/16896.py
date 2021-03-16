import sys
from itertools import permutations

input = sys.stdin.readline

N , K = map(int ,input().split())
winning_info = [[0,0,0]]
for _ in range(N):
    winning_info.append(list(map(int , input().split())))

for lis in winning_info:
    lis.insert(0,0)

toA = list(map(int ,input().split()))
toB = list(map(int ,input().split()))

tmp_list = [i+1 for i in range(N)]
perm = permutations(tmp_list , N)

def simulation(perset):
## 0 - 지우 ,  1 - 경희 , 2- 민호 
    winning_counter = [0 , 0 , 0]
    rcp_order = [0 , 0 , 0]
    flag_order = 2
    while True:
        if winning_counter[0] == K:
            return True
        if rcp_order[0] == N or winning_counter[1] == K or winning_counter[2] == K:
            return False
        if flag_order == 2:
            ta , tb = rcp_order[0] , rcp_order[1]
            victory = winning_info[perset[ta]][toA[tb]]
            rcp_order[0]+=1
            rcp_order[1]+=1
            if victory == 2:
                winning_counter[0]+=1
                flag_order = 1
            else:
                winning_counter[1]+=1
                flag_order = 0
        elif flag_order == 1:
            ta , tb = rcp_order[0] , rcp_order[2]
            victory = winning_info[perset[ta]][toB[tb]]
            rcp_order[0]+=1
            rcp_order[2]+=1
            if victory == 2:
                winning_counter[0]+=1
                flag_order = 2
            else:
                winning_counter[2]+=1
                flag_order = 0
        else:
            ta , tb = rcp_order[1] , rcp_order[2]
            victory = winning_info[toA[ta]][toB[tb]]
            rcp_order[1]+=1
            rcp_order[2]+=1
            if victory == 2:
                winning_counter[1]+=1
                flag_order = 2
            else:
                winning_counter[2]+=1
                flag_order = 1
    return False


res_flag = False
for elem in list(perm):
    if simulation(elem):
        res_flag = True
        break

if res_flag == True:
    print(1)
else:
    print(0)



    



    
    