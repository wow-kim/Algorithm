from collections import deque
def solution(msg):

    dic = {}
    for i, word in enumerate(range(ord('A'), ord('Z')+1)):
        dic[chr(word)] = i+1

    output = []

    msg = deque(msg)
    while msg:

        w = msg.popleft()
        while msg:
            temp = msg[0]
            if w + temp not in dic.keys():
                output.append(dic[w])
                dic[w+temp] = len(dic.keys())+1
                break
            else:
                w = w + msg.popleft()

        if not msg:
            output.append(dic[w])                

    return output
