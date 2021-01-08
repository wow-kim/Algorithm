def solution(name):
    answer = 0
    for n in name: # 상하 이동
        answer += min(ord(n)-ord("A"), 26-(ord(n)-ord("A")))

    first_A = name.find("A",1)
    if first_A == -1 : 
        return answer + len(name)-1

    next_ = [i for i,j in enumerate(name) if j != "A" and i > first_A][0]
    return min(answer + len(name)-1, answer + 2*(first_A-1) + len(name)-next_)

# 좀 잘한것 같다.
