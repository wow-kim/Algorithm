def solution(s):
    
    units = []
    for num in s[2:-2].split("},{"):
        num = list(map(int, num.split(",")))
        units.append(num)

    units = sorted(units, key=lambda x: len(x))  

    answer = []

    for unit in units:
        for u in unit:
            if u not in answer:
                answer.append(u)

    return answer

#-----------------------------------------------
import re
from collections import Counter

def solution(s):
    
    s = Counter(re.findall('\d+', s))
    return list(map(int, [k for k, v in sorted(s.items(), key=lambda x: x[1], reverse=True)]))

