def solution1(s):
    
    answer = 1
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            left, right = i, i+1
            while (left >= 0) & (right <= len(s)-1):
                if s[left] == s[right]:
                    answer = max(answer, right - left + 1)
                    left -= 1
                    right += 1
                else:
                    break
        left, right = i, i
        while (left >= 0) & (right <= len(s)-1):
            if s[left] == s[right]:
                answer = max(answer, right - left + 1)
                left -= 1
                right += 1
            else:
                break

    return answer

def longest_palindrom(s):
    return len(s) if s[::-1] == s else max(longest_palindrom(s[:-1]), longest_palindrom(s[1:]))