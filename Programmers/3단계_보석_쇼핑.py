### 시간 초과(효율성 0점)
def solution1(gems):
    gem_set = set(gems)
    answer = [0, len(gems)]
    
    for i in range(len(gems)):
        j = i
        gems_temp = set()
        while (j < len(gems)) & (i-j+1 < answer[1] - answer[0]):
            gems_temp.add(gems[j])
            if gems_temp == gem_set:
                answer = min(answer, [i, j+1], key = lambda x: x[1] - x[0])
                break
            j += 1
    
    answer[0] += 1
    return answer


### 시간 초과(효율성 점수 8.9점)
def solution2(gems):
    gem_set = set(gems)
    answer = [0, len(gems)]
    
    i = 0
    while i < len(gems):
        j = i
        flag = False
        gems_temp = set()
        while (j < len(gems)) & (i-j+1 < answer[1] - answer[0]):
            gems_temp.add(gems[j])
            if gems_temp == gem_set:
                answer = min(answer, [i, j+1], key = lambda x: x[1] - x[0])
                flag = True
                break
            j += 1
            
        i += 1
        if flag:
            k = 1
            while set(gems[i+k:j+1]) == gem_set:
                k += 1
            else:
                k -= 1
            i += k

    answer[0] += 1
    return answer
    
### 투 포인(통과)
def solution3(gems):
    n = len(set(gems))
    answer = [0, len(gems)-1]
    start, end = 0, 0
    dic = {gems[0]: 1}
    while start < len(gems) and end < len(gems):
        if len(dic) == n:
            answer = min(answer, [start, end], key = lambda x: x[1] - x[0])
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
            start += 1
        else:
            end += 1
            if end == len(gems):
                break
            else:
                if dic.get(gems[end]) is None:
                    dic[gems[end]] = 1
                else:
                    dic[gems[end]] += 1

    answer[0] += 1
    answer[1] += 1
    return answer