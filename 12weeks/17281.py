## TLE CODE
"""
import sys
from itertools import permutations
from collections import deque
input = sys.stdin.readline

N = int(input())
innings_results = [list(map(int,input().split())) for _ in range(N)]
OutCount = 0
TotalPoint = 0
base_status = [0,0,0]
ans = 0

players_order = [0,1,2,4,5,6,7,8]
perm = permutations(players_order,8)

for player in list(perm):
    for idx in range(N):
        base_status = [0,0,0]
        OutCount = 0
        ans = max(ans , TotalPoint)
        TotalPoint = 0
        while True:
            if OutCount == 3:
                break

            for j_idx in range(9):
                if j_idx == 0:
                    res = innings_results[idx][3]
                else:
                    j_idx -= 1
                    res = innings_results[idx][player[j_idx]]

                if res == 0:
                    OutCount += 1
                
                elif res == 1:
                    if base_status[0] == 0:
                        base_status[0] = 1
                    else:
                        if base_status[2] == 1:
                            TotalPoint += 1
                        for based in range(2 , 0 , -1):
                            base_status[based] = base_status[based-1]
                        base_status[0] = 1
                
                elif res == 2:
                    if base_status[1] == 0:
                        base_status[1] = 1
                    else:
                        if base_status[1] == 1:
                            TotalPoint += 1
                            base_status[1] = 1
                        if base_status[2] == 1:
                            TotalPoint += 1
                            if base_status[0] == 1:
                                base_status[2] = 1
                elif res == 3:
                    if base_status[2] == 0:
                        base_status[2] == 1
                    else:
                        if base_status[2] == 1:
                            TotalPoint += 1
                            base_status[2] = 1
                        if base_status[1] == 1:
                            TotalPoint += 1
                elif res == 4:
                    TotalPoint += 1
                    for k_idx in range(3):
                        if base_status[k_idx] == 1:
                            TotalPoint += 1
                        base_status = [0,0,0]

print(ans)
"""

### best code 
import sys
from itertools import permutations
end = int(sys.stdin.readline())
inning = [list(map(int, sys.stdin.readline().split())) for _ in range(end)]

max_score = 0

def game(line_ups):
    hitter_idx = 0
    score = 0
    for each_inning in inning:
        outcount = 0
        b1, b2, b3 = 0, 0, 0
        while outcount < 3:
            if each_inning[line_ups[hitter_idx]] == 0:
                outcount += 1
            elif each_inning[line_ups[hitter_idx]] == 1:
                score += b3
                b1, b2, b3 = 1, b1, b2
            elif each_inning[line_ups[hitter_idx]] == 2:
                score += (b2 + b3)
                b1, b2, b3 = 0, 1, b1
            elif each_inning[line_ups[hitter_idx]] == 3:
                score += (b2 + b3 + b1)
                b1, b2, b3 = 0, 0, 1
            elif each_inning[line_ups[hitter_idx]] == 4:
                score += (1 + b1 + b2 + b3)
                b1, b2, b3 = 0, 0, 0
            
            hitter_idx = (hitter_idx + 1) % 9
    return score
        
for line_ups in permutations(range(1,9), 8):
    line_ups = list(line_ups[:3]) + [0] + list(line_ups[3:])
    max_score = max(max_score, game(line_ups))

print(max_score)