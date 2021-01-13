## Programmers 실패율
## https://programmers.co.kr/learn/courses/30/lessons/42889?language=python3

def solution(N , stages):
    answer = []

    ## we don't have to consider N+1 stage runner
    ## just count total runner in stages and clearer 

    for i in range(1 , N+1):
        ##operand => stage clear guy count
        ##divider => reach ith stage count
        divider = 0
        operand = 0

        ##in this case O(n^2) is also passed
        ##use count method is better way
        for j in stages:
            if i <= j:
                divider += 1
            if i == j:
                operand += 1
                
        ## get rid of division by zero
        if divider == 0 or operand == 0:
            answer.append([i , 0])
        else:
            res = operand / divider
            answer.append([i , res])
    answer.sort(key=lambda x : -int(x[1]))
    return answer
