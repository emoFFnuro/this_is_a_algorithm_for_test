import re
n = int(input())
pattern = "(100+1+|01)+"
for i in range(n):
    tmp_str = input()
    p = re.compile(pattern)
    res = p.fullmatch(tmp_str)
    if res:
        print('YES')
    else:
        print('NO')