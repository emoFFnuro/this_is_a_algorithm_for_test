import sys

N, K = list(map(int, sys.stdin.readline().split()))
table = sys.stdin.readline().strip()

def solution():
    eated = [0] * N
    answer = 0
    for i in range(N):
        if table[i] == 'P':
            for idx in range(-K, K + 1):
                ni = i + idx
                if 0 <= ni < N and table[ni] == 'H' and not eated[ni]:
                    eated[ni] = 1
                    answer += 1
                    break
    return answer

print(solution())