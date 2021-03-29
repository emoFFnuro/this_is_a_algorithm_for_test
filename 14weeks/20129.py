## input
op_order = list(map(int , input().split()))
exp_str = input()

orders = ['+' , '-' , '*' , '/']
## for storing number and oper
nums = list()
opers = list()
zerocheckers = ''

def calc(num1 , num2 , oper):
    if oper == '+':
        return num1 + num2
    elif oper == '-':
        return num1 - num2
    elif oper == '*':
        return num1 * num2
    elif oper == '/':
        if num1 * num2 >= 0:
            return num1 // num2
        else:
            if abs(num1 % num2):
                return(num1//num2) + 1
            else:
                return(num1//num2)

for i in range(len(exp_str)):
    if '0' <= exp_str[i] <= '9':
        zerocheckers += exp_str[i]
    else:
        nums.append(int(zerocheckers))
        opers.append(exp_str[i])
        zerocheckers = ''

nums.append(int(zerocheckers))
            
input_oper = ['' , '' , '' ,'']

for idx , pr in enumerate(op_order):
    input_oper[pr-1] = orders[idx]

for i in range(3 , -1 ,-1):
    tmp = input_oper[i]
    for i in range(len(opers)-1 , -1 , -1):
        if opers[i] == tmp:
            res = calc(nums[i+1] , nums[i] , opers[i])
            del opers[i]
            nums[i] = res
            del nums[i+1]

if len(opers):
    res = calc(nums[1] ,nums[0] , opers[0])
else:
    res = nums[0]

print(res)
