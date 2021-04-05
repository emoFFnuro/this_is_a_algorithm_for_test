import sys

input = sys.stdin.readline

n = int(input())
pr_list = [list(map(int ,input().split())) for _ in range(n)]
pr_list.sort()

answer = []

for li in pr_list:
    deadline = li[0]
    answer.append(li[1])

    while deadline < len(answer):
        answer.remove(min(answer))
    
print(sum(answer))