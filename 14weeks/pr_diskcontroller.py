import heapq

def solution(jobs):
    answer , now , i = 0,0,0
    start = -1
    hp = []

    while i < len(jobs):
        for j in jobs:
            if start < j[0] <= now:
                heapq.heappush(hp , [j[1] , j[0]])
        
        if len(hp) > 0:
            current = heapq.heappop(hp)
            start = now
            now += current[0]
            answer += (now - current[1])
            ## when successfully done add one in i 
            i += 1
        else:
            now += 1
        
    return int(answer / len(jobs))