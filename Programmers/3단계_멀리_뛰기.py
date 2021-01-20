def solution(n):
    
    def fib(N):
        x, y = 1, 1
        for _ in range(N):
            x, y = y, x+y
        return x
    
    return fib(n)%1234567