import sys , heapq

input = sys.stdin.readline
N,M= map(int, input().split())
TC_MAP = [list(map(int, input().rstrip())) for _ in range(M)]
visit = [[0] * N for _ in range(M)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def dijkstra():
    q = []
    heapq.heappush(q, [0, 0, 0]) 
    visit[0][0] = 1

    while q:
        cnt, x, y = heapq.heappop(q)  
        for k in range(4):
            nx, ny = x + dx[k], y + dy[k]
            if x == N - 1 and y == M - 1: 
                print(cnt)
                break
            if 0 <= nx < N and 0 <= ny < M and not visit[nx][ny]:
                visit[nx][ny] = 1

                if TC_MAP[nx][ny]:  
                    heapq.heappush(q, [cnt + 1, nx, ny])
                else:  
                    heapq.heappush(q, [cnt, nx, ny])

dijkstra()
