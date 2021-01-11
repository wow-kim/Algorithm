def solution(s):
    
    s = list(s)
    stack = [s.pop()]
    while s:
        if stack:        
            if stack[-1] == s[-1] :
                stack.pop()
                s.pop()
                continue
        stack.append(s.pop())

    return int(stack == [])