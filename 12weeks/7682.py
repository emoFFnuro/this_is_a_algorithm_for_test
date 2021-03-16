import sys

def check(st):
    r = []
    for i in range(0, 7, 3):
        if st[i] != "." and st[i] == st[i + 1] and st[i + 1] == st[i + 2]:
            r.append(st[i])
    for i in range(3):
        if st[i] != "." and st[i] == st[i + 3] and st[i + 3] == st[i + 6]:
            r.append(st[i])

    if st[0] != "." and st[0] == st[4] and st[4] == st[8]:
        r.append(st[0])
    if st[2] != "." and st[2] == st[4] and st[4] == st[6]:
        r.append(st[2])
    return r

while True:
    input_str = input()
    if input_str == "end":
        exit(0)
    x, o = 0, 0
    for i in input_str:
        if i == 'X':
            x += 1
        elif i == 'O':
            o += 1
    result = check(input_str)
    if "X" not in result and "O" not in result and x == 5 and o == 4:
        print("valid")
    elif "X" in result and "O" not in result and x == o + 1:
        print("valid")
    elif "O" in result and "X" not in result and x == o:
        print("valid")
    else:
        print("invalid")