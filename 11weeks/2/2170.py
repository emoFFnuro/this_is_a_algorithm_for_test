import sys
input = sys.stdin.readline

### don't use list just add when case is out
def solution(lines,N):
    lines.sort(key = lambda x:(x[0],-x[1]))
    answer = lines[0][1]-lines[0][0]
    tempstart=lines[0][0]; tempend=lines[0][1]
    for i in range(1,N):
        start = lines[i][0]
        end = lines[i][1]
        if start >= tempend:
            answer += end-start
            tempstart = start; tempend = end
        elif tempstart <= end <= tempend:
            continue
        elif start <= tempend and end >= tempend:
            answer+= end - tempend
            tempend=end
    return answer

def solve():
    N = int(input())
    lines = list()
    for i in range(N):
        line = list(map(int,(input().split())))
        lines.append(line)
    print(solution(lines,N))
solve()
### this is MLE .... find out another method
"""
def getLength(sp , ep):
    
    if len(answer_list) == 0:
        answer_list.append([sp,ep])
        return 0

    for al in answer_list:
        prev_sp , prev_ep = al[0] , al[1]
        ## case.1
        if prev_sp < sp < prev_ep:
            if prev_ep <= ep:
                al[1] = ep
        ## case.2
        if prev_sp == sp:
            if prev_ep <= ep:
                al[1] = ep
        elif prev_ep == sp:
            al[1] = ep
        ## case.3
        if sp <= prev_sp and ep >= prev_ep:
            al[0] , al[1] = sp , ep
        ## case.4
        if prev_ep <= sp or prev_sp >= ep:
            answer_list.append([sp,ep])

def getCalc(arr):
    ans = 0
    for pair in arr:
        tmpx , tmpy = pair[0] , pair[1]
        ans += (tmpy - tmpx)
    return ans

for _ in range(n):
    sp , ep = map(int , input().split())
    getLength(sp,ep)

total_ans = 0
total_ans = getCalc(answer_list)
print(total_ans)
"""

