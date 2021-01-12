# BOJ.10825 - 국영수  
# https://www.acmicpc.net/problem/10825

## 1.get tc count from console
n = int(input())
students = list()

## 1-2. get tc from console
##  -> get string tc and make it list based on space
for _ in range(n):
    students.append(input().split())

## 2. sort by using lambda
## https://docs.python.org/3/tutorial/controlflow.html#lambda-expressions
students.sort(key = lambda x: (-int(x[1]) , int(x[2]) , -int(x[3]) , x[0]))

## 3. print answer(only name allowed)
for i in students:
    print(i[0])

