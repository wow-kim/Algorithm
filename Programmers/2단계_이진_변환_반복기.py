def solution(s):
    conversion = 0
    eliminated = 0
    while s != "1":
        eliminated += len(s)
        s = "".join([i for i in s if i=="1"])
        eliminated -= len(s)
        s = format(len(s),"b")
        conversion += 1

    return [conversion, eliminated]

print(solution("110010101001"))