import sys
input = sys.stdin.readline
def find(parent , x):
    if x != parent[x]:
        return find(parent , parent[x])
    return parent[x]

def union(parent , a , b):
    a , b = find(parent , a) , find(parent , b)
    if a < b:
        parent[b] = a
    elif a == b:
        return
    elif a > b:
        parent[a] = b

V , E = map(int,input().split())
parent = [0] * (V + 1)

edges = list()
res = 0

for i in range(1 , V+1):
    parent[i] = i

for _ in range(E):
    a , b , cost = map(int , input().split())
    edges.append([cost , a , b])

edges.sort()
last = 0

for edge in edges:
    cost , a , b = edge
    if find(parent , a) != find(parent , b):
        union(parent , a, b)
        res += cost
        last = cost
print(res - last)

