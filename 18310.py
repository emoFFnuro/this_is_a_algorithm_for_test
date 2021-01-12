## BOJ.18310 안테나
## https://www.acmicpc.net/problem/18310


## 비슷한문제도 존재하지만 이 경우는 안테나의 유효거리같은 조건이 없으므로
## 무조건 중간값에 위치하는것이 최소값이다  
n = int(input())

## to eliminate same number use map
n_list = list(map(int, input().split()))

n_list.sort()

## print(n_list)

answer = n_list[(n-1)//2]
print(answer)