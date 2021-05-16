def check(s):    
    dic = {'[':0, '{':0, '(':0}
    pair = {']':'[', ')':'(', '}':'{'}
    stack = []

    for bracket in s:
        if bracket in dic.keys():
            stack.append(bracket)
            dic[bracket] += 1
        else:
            p = pair[bracket]
            if dic[p] == 0:
                return False
            else:
                f = stack.pop()
                if f != p:
                    return False
                else:
                    dic[p] -= 1

    if sum(dic.values()):
        return False
    else:
        return True

def rotate(s):
    pre = s[0]
    return s[1:] + pre

def solution(s):
    answer = 0
    if len(s) == 1:
        return answer
    for _ in range(len(s)):
        s = rotate(s)
        if check(s):
            answer += 1
    return answer