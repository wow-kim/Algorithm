# 1. words에 바꿀 수 있는 단어가 있는 지 확인
# 2. 바꿀 수 있는 모든 단어로 변경
# 3. 변경 된 단어가 TARGET이랑 같으면 COUNT 반환

from collections import deque
def changeable_words(s, words):
    result = []
    for i in range(1, len(s)+1):
        result.extend([word for word in words if word[:i-1] + word[i:] == s[:i-1] + s[i:]])
    return result

def solution(begin, target, words):
    if target not in words:
        return 0

    words = set(words)
    q = deque()
    q.append([begin, words, 0]) # 0 : count
    answer = 1000000
    while q:
        b, ws, count = q.popleft()
        if count >= answer:
            continue
        if b == target:
            answer = min(answer, count)
        for w in changeable_words(b, ws):
            q.append([w, set(ws) - set([w]), count+1])

    if answer == 1000000:
        return 0
    else:
        return answer
