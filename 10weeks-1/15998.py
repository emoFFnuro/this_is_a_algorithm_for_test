import sys

def gcd(a,b):
    while (b != 0):
        temp = a % b
        a = b
        b = temp
    return abs(a)

n = int(input())
min_b = pow(10,18)
lastest_b = 0
pay = None
validate = True

for i in range(n):
    a , b = map(int , sys.stdin.readline().split())
    if a + lastest_b < 0 :
        temp = b-a-lastest_b
        if b != 0 and b < min_b:
            min_b = b
        if pay == None:
            pay = temp
        else:
            pay = gcd(pay , temp)
            if pay <= min_b and min_b != pow(10,18):
                validate = False
                break

    else:
        if lastest_b + a != b:
            validate = False
            break
    lastest_b = b
if validate and pay != None : print(pay)
elif validate and pay == None : print(1)
else : print(-1)

