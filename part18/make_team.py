import sys
input = sys.stdin.readline

N , M = map(int , input().split())
students = [0] * (N+1)

def find(parent , x):
    if parent[x] != x:
        return find(parent , parent[x])
    return parent[x]

def union(parent , a , b):
    a  , b = find(parent , a) , find(parent , b)
    if a < b:
        parent[b] = a
    elif a == b:
        return
    elif a > b:
        parent[a] = b

for idx in range(M):
    oper , a , b = map(int ,input().split())
    if oper == 0:
        union(students , a , b)
    elif oper == 1:
        if find(students , a) == find(students , b):
            print('YES')
        else:
            print('NO')
        