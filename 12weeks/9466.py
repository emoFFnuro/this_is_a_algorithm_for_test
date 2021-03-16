import sys
sys.setrecursionlimit(10**6)

input = sys.stdin.readline
def dfs(start_node):
    global res
    visited[start_node] = 1
    cycle.append(start_node)
    next_node = graph_info[start_node]

    if visited[next_node]:
        if next_node in cycle:
            res += cycle[cycle.index(next_node):]
        return
    else:
        dfs(next_node)


tc = int(input())
for idx in range(tc):
    res = list()
    n = int(input())
    visited = [1] + [0] * (n+1)
    graph_info = [0] + list(map(int ,input().split()))
    for idx in range(1 , n+1):
        if not visited[idx]:
            cycle = []
            dfs(idx)    
    print(n - len(res))