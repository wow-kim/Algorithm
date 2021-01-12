def solution(s):
    s = s.lower().split(" ")[::-1]
    
    answer = ""
    while s:
        word = s.pop()
        if word:
            answer += word[0].upper() + word[1:]+" "
        else:
            answer += " "
    return answer[:-1]

#---------------------------------------------------

def solution(s):
    return s.title()