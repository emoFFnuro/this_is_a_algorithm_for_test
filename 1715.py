## BOJ.1715
## https://www.acmicpc.net/problem/1715
import heapq


## basic idea 
## -> A+B 의 비교 횟수가 A+B이므로 최솟 비교값을 찾기 위해선 작은것 끼리 더해가야 한다
## use minheap or sort(ascending) when every push A+B 
def solution():
    answer = 0
    N = int(input())
    deck_list = list()
    for _ in range(N):
        heapq.heappush(deck_list , int(input()))

## when only one card list in deck there is no need to compare
    if len(deck_list) == 1:
        return 0
    else:
        while(len(deck_list) > 1):
            first = heapq.heappop(deck_list)
            second = heapq.heappop(deck_list)
            answer += first + second
            heapq.heappush(deck_list , first+second)
        return answer

print(solution())