from typing import List

class Solution:
    def singleNumber(self, nums:List[int]) -> int:
        """
        70. 싱글 넘버(leetcode : 136)
        a. XOR를 이용 
        같은 값이면 0을 반환
        """
        result = 0
        for num in nums:
            result ^= num
        return result

    def hammingDistance(self, x:int, y:int) -> int:
        """
        71. 해밍 거리(leetcode : 461)
        a. XOR를 이용
        두 정수끼리 몇 비트가 다른지 계산
        """
        return bin(x ^ y).count("1")
    
    def hammingWeight(self, n:int) -> int:
        """
        74. 1비트의 개수(leetcode : 191)
        a. 비트 연산
        """
        count = 0
        while n:
            n &= n-1
            count += 1
        return count
    