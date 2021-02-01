# when i is 1 => 1
# case 2 => 3
# case 3 => 5

# 1 -> (2x1)
# 2 -> (2x1 , 2x1) , (2x2) , (1x2 , 1x2)
# 3 -> (2x1 , 2x1 , 2x1) , (1x2 , 2x1 ,2x1) , (2x1 , 2x1 , 1x2) , (2x2 , 2x1) , (2x1 , 2x2)

n = int(input())

d = [0] * 1001

d[1] = 1
d[2] = 3
for i in range(3, n + 1):
    d[i] = (d[i - 1] + 2 * d[i - 2]) % 796796

print(d[n])