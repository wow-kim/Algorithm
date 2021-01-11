def solution(n):
    
    def iterative(i):
        if i <= 2 :
            value = 1
        else:
            value1 = 1
            value2 = 1
            for j in range(3,i+1):
                value = value1 + value2
                value1 = value2
                value2 = value
        return value
    return iterative(n) % 1234567

#---------------------------------------

def fibonacci(num):
    a,b = 0,1
    for i in range(num):
        a,b = b,a+b
    return a
