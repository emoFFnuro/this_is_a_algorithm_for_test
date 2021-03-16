import sys

input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]

for _ in range(n):
    path = list(map(int , input().split()))
    len_path = len(path)
    for i in range(1 , len_path//2):
        graph[path[0]].append([path[2*i-1],path[2*i]])

results = [-1] * (n+1)
results2 = [-1] * (n+1)

def dfs(start_node ,result):
    for to , val in graph[start_node]:
        if result[to] == -1:
            result[to] = result[start_node] + val
            dfs(to , result)

results[1] = 0
dfs(1 , results)

maxIdx = results.index(max(results))
results2[maxIdx] = 0
dfs(maxIdx , results2)
print(max(results2))

