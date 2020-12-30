def solution(clothes):
    dict = {}
    for c in clothes:
        dict[c[1]] = dict.get(c[1], 0) +1
    answer = 1
    for i in dict.values():
        answer = answer*(i+1)
    return answer - 1