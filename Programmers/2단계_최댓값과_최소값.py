
def solution(s):
    a = s.split(" ")
    a = [int(i) for i in a]
    return " ".join([str(min(a)), str(max(a))])