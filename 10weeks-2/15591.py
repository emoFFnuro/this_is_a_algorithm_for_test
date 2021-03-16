import sys
from collections import defaultdict, deque

input = sys.stdin.readline

N , E = map(int , input().split())
map_dict = defaultdict(list)

for _ in range(N-1):
    p , q , r = map(int , input().split())
    map_dict[p-1].append((q-1 , r))
    map_dict[q-1].append((p-1 , r))
    

def bfs(start_node,k,map_dict):
    q= deque()
    q.append((start_node , float('inf')))
    visited = [False] * (N + 1)
    visited[start_node] = True
    count = 0

    while q:
        pop_node , min_dist = q.popleft()
        for next_node , dist in map_dict[pop_node]:
            if visited[next_node] == True : continue
            if min_dist > dist:
                q.append((next_node , dist))
                if dist >= k:
                    count += 1
            else:
                q.append((next_node , min_dist))
                if min_dist >= k:
                    count += 1
            visited[next_node] = True
    
    return count


for _ in range(E):
    k , v = map(int , input().split())
    print(bfs(v-1 , k , map_dict))