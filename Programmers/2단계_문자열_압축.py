def solution(s):
    
    answer = len(s)

    for i in range(1, len(s)//2+1):
        compressed = ""
        temp = s[:i]
        count = 1
        words = s[i:]
        for _ in range(len(s)//i+1):

            word = words[:i]
            words = words[i:]
            if word == temp:
                count +=1
            else:
                if count == 1:
                    compressed += temp
                else:
                    compressed += str(count) + temp
                temp = word
                count = 1

        answer = min(answer, len(compressed))

    return answer
