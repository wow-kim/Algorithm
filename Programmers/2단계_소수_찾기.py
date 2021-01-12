from itertools import permutations
def solution(numbers):

    def isPrime(number):
        if number != 1 and number != 0:
            for n in range(2,number):
                if number % n == 0:
                    return False
        else:
            return False
        return True

    nums = []
    for i in range(1,len(numbers)+1):
        nums += list(permutations(numbers, i))

    answer = set()
    for n in nums:
        value = int("".join(n))
        if isPrime(value):
            answer.add(value) 

    return len(answer)