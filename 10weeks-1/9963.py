def promising(i , col):
    k = 1
    flag = True
    while k<i and flag:
        if col[i] == col[k] or abs(col[i] - col[k]) == abs(i-k):
            flag = False
        k +=1
    return flag

def n_queens(i,col):
    global count
    n = len(col) - 1
    if promising(i,col):
        print(col)
        if i==n:
            count+=1
        else:
            for j in range(1 , n+1):
                col[i+1] = j
                n_queens(i+1 ,col)

n = int(input())
col = [0] * (n+1)
count = 0

n_queens(0 , col)

