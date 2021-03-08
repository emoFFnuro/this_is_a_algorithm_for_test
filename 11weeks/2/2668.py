## check cycle...

N = int(input())
graph_info = [[] for _ in range(N+1)]
for i in range(N):
    graph_info[i+1].append(int(input()))
res = list()

def dfs(v,i):
    visited[v] = True

    for next_node in graph_info[v]:
        if not visited[next_node]:
            dfs(next_node , i)
        elif visited[next_node] and next_node == i:
            res.append(next_node)
    
for i in range(1 , N+1):
    visited = [False] * (N+1)
    dfs(i , i)

print(len(res))
for idx in range(len(res)):
    print(res[idx])