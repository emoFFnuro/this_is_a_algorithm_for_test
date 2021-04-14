from itertools import combinations

l,c = map(int , input().split())
alpha = list(map(str , input().split()))
vowel = ['a','e','i','o','u']

alpha_to_num = []
for i in alpha:
    alpha_to_num.append(ord(i) - ord('a'))

alpha_to_num.sort()
alpha.clear()
for i in alpha_to_num:
    alpha.append(chr(i + ord('a')))

res = []
comb = list(map(''.join , combinations(alpha,l)))

for word in comb:
    cnt_vowel = 0
    cnt_conso = 0
    for char in word:
        if char in vowel:
            cnt_vowel+=1
        elif char not in vowel:
            cnt_conso+=1
    if cnt_vowel >= 1 and cnt_conso >=2 :
        res.append(word)

for i in res:
    print(i)
