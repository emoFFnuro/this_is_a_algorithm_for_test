valid_chs = [chr(i) for i in range(ord('a') , ord('z')+1)]
valid_chs += ['.','-','_']
valid_chs += [str(i) for i in range(10)]

def kill(new_id):
    tmp = ''
    for ch in new_id:
        if ch in valid_chs:
            tmp += ch
    return tmp

def pointerConverter(new_id):
    if not new_id:
        return ""
    cnt , tmp = 0 , ''
    
    for ch in new_id:
        if ch == '.':
            cnt += 1
            if cnt == 2:
                cnt = 1
                continue
        else:
            cnt = 0
        tmp += ch
        
    return tmp
def lrstrip(new_id):
    if not new_id or (len(new_id) == 1 and new_id[0] == '.'): return ''
    tmp = list(new_id)
    if new_id[0] == '.': del tmp[0]
    if new_id[-1] == '.': del tmp[-1]
    return ''.join(tmp)

def solution(new_id):
    ## 1. to convert it lower
    new_id = new_id.lower()
    ## 2. delete all thing without a-z , digits , - , _ , .
    answer = kill(new_id)
    ## 3. .. -> .
    answer = pointerConverter(answer)
    ## 4. remove first , last . 
    answer = lrstrip(answer)
    ## 5. check empty string
    if not answer:
        answer = 'a'
    ## 6. check length and make it short
    if len(answer) > 15:
        answer = answer[:15]
    if answer[-1] == '.':
        answer = answer[:14]
    ## check length of answer. if that is under 2. just add last character
    if len(answer) < 3:
        for i in range(len(answer) , 3):
            answer += answer[-1]
    return answer