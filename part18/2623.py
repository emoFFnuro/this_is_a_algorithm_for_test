
N, M = map(int, input().split())
pds = [[] for _ in range(N+1)]  
inDegree = [0 for _ in range(N+1)]

for i in range(M):
    temp = list(map(int, input().split()))
    for j in range(temp[0]-1):
        pds[temp[j+1]] += [temp[j+2]]

for n in range(1, N+1):
    if pds[n]:
        for i in pds[n]:
            inDegree[i] += 1

q = []
res = []
isCycle = False

for i in range(1, len(inDegree)):
    if inDegree[i] == 0:
        q.append(i)

if not q:
    q.append(inDegree[0])


for _ in range(N):
    if not q:  
        isCycle = True
        break
    v = q.pop(0)
    res.append(v)

    for u in pds[v]:
        inDegree[u] -= 1
        if inDegree[u] == 0:
            q.append(u)
            
if isCycle:
    print(0)
else:
    for r in res:
        print(r)
