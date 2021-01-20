def solution(n):
    
    def fib(N):
        x, y = 1, 1
        for i in range(0, N):
            x, y = y, x + y
        return x
    return recur(n) % 1000000007