import sys
input = sys.stdin.readline

n , m , t = map(int,input().split())
circular_list = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    circular_list.append(tmp)
xi,di,ki = map(int,input().split())

def rotatePlate(dir , select):
    totaltmp = list()
    ## 0 is clockwise 1 is counter-clockwise
    if dir == 0:
        for cirp in circular_list:
            tmp = [cirp[len(cirp)-1]]+ cirp[0:n-1]
            totaltmp.append(tmp)   
    else:
        for cirp in circular_list:
            tmp = cirp[0:n-1] + [cirp[len(cirp)-1]]
            totaltmp.append(tmp)
    
    for i in range(n):
        if (i+1) % select != 0:
            totaltmp[i] = circular_list[i]
    
    return totaltmp

"""
circular_list = rotatePlate(0 , 2)
print(circular_list)
"""



