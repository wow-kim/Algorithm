from math import gcd
def solution(arr):
    def lcm(a, b):
        return a * b / gcd(a, b)

    answer = arr[0]
    for a in arr[1:]:
        answer = lcm(int(answer), a)

    return answer

#-----------------------------------

def solution(arr):
    a = arr[0]
    for b in arr[1:]:
        temp = a * b
        while (b != 0):
            a, b = b, a % b

        a = temp // a

    answer = a
    return answer