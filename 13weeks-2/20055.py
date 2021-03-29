import sys
from collections import deque

N , K = map(int , input().split())
pos_list = list(map(int ,input().split()))
robot_list = [0] * (2*N)
robots = deque()
cnt =  0
while True:
    cnt+=1
    ## rotate whole position
    pos_list = pos_list[-1:] + pos_list[:-1]
    robot_list = robot_list[-1:] + robot_list[:-1]

    if robot_list[len(robot_list) // 2 - 1]:
        robot_list[len(robot_list) // 2 - 1] = 0
    
    robots_len = len(robots)
    for _ in range(robots_len):
        tx = robots.popleft()
        tx += 1

        if tx == len(pos_list) // 2 - 1:
            continue

        rx = tx + 1

        if not robot_list[rx] and pos_list[rx] > 0:
            if rx == len(pos_list) // 2 - 1:
                robot_list[tx] = 0
            else:
                robots.append(rx)
                robot_list[tx] , robot_list[rx] = 0 , 1
            pos_list[rx] -= 1
        else:
            robots.append(tx)
        
    if pos_list[0] > 0 and not robot_list[0]:
            robots.append(0)
            robot_list[0] = 1
            pos_list[0] -= 1
        
    if pos_list.count(0) >= K:
        break
print(cnt)