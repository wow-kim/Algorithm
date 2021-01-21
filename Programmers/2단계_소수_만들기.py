import itertools
import math
def solution(nums):

    def is_prime(x):
        for i in range(2, int(math.sqrt(x))+1):
            if x % i == 0:
                return False
        return True

    odds = [n for n in nums if n%2 != 0]
    even = [n for n in nums if n%2 == 0]

    #홀 홀 홀
    count = 0
    if len(odds) >= 3:
        for three_odd in itertools.combinations(odds, 3):
            if is_prime(sum(three_odd)):
                count += 1
    #홀 짝 짝
    if len(odds) >= 1 and len(even) >= 2:
        for odd in odds:
            for two_even in itertools.combinations(even,2):
                if is_prime(sum(two_even)+odd):
                    count += 1

    return count
