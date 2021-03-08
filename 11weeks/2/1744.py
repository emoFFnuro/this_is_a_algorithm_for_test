from collections import deque

n = int(input())
arr = [int(input()) for _ in range(n)]

arr.sort()
q = deque(arr)
positive_number = list()
negative_number = list()
last = list()
ans = 0
while q:
    num = q.popleft()
    if num > 1:
        positive_number.append(num)
    elif num <= 0:
        negative_number.append(num)
    else:
        last.append(num)

positive_number.sort(reverse=True)
negative_number.sort()

for i in range(0 , len(negative_number) , 2):
    if i + 1 < len(negative_number):
        ans += negative_number[i] * negative_number[i+1]
    else:
        ans += negative_number[i]

for i in range(0, len(positive_number) , 2):
    if i + 1 < len(positive_number):
        ans += positive_number[i] * positive_number[i+1]
    else:
        ans += positive_number[i]

ans += sum(last)


print(ans)