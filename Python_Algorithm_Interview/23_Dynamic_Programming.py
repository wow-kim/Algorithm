# 다이나믹 프로그래밍
# 반복적으로 동일한 하위 문제로 나누어 해결한 결과를 저장해뒀다가 나중에 큰 문제의 결과와 합하여 풀이
# 최적 부분 구조(Optimal Substructure)를 갖고 있는 문제를 풀이할 수 있다.

# 메모이제이션(Memoization)(하향식 접근법)
# 타뷸레이션(Tabulation)(상향식 접근법)

from typing import List
import collections
import sys

class Solution:
    def fib_a(self, N:int):
        """
        85. 피보나치 수(leetcode : 509)
        a. 재귀 구조
        """
        if N <= 1:
            return N
        return self.fib(N-1)+self.fib(N-2)
    
    dp = collections.defaultdict(int)
    def fib_b(self, N:int):
        """
        85. 피보나치 수(leetcode : 509)
        b. 메모이제이션
        한번 계산한 수는 더 이상 계산하지 않아 더 효율적
        """
        if N <= 1:
            return N
        
        if self.dp[N]:
            return self.dp[N]
        self.dp[N] = self.fib_b(N-1) + self.fib_b(N-2)
        return self.dp[N]
    
    dp = collections.defaultdict(int)
    def fib_c(self, N:int):
        """
        85. 피보나치 수(leetcode : 509)
        c. 타뷸레이션
        """   
        self.dp[1] = 1
        
        for i in range(2, N+1):
            self.dp[i] = self.dp[i-1] + self.dp[i-2]
        return self.dp[N]
    
    def fib_d(self, N:int):
        """
        85. 피보나치 수(leetcode : 509)
        d. 두 변수만 사용해 공간 절약
        공간 복잡도 O(N) -> O(1)
        """   
        x, y = 0, 1
        for i in range(0, N):
            x, y = y, x + y
        return x
    
    def maxSubArray_a(self, nums:List[int]):
        """
        86. 최대 서브 배열(leetcode : 53)
        a. 메모이제이션
        """
        for i in range(1, len(nums)):
            nums[i] += nums[i-1] if nums[i-1] > 0 else 0
        return max(nums)

    def maxSubArray_b(self, nums:List[int]):
        """
        86. 최대 서브 배열(leetcode : 53)
        b. 카데인 알고리즘
        """
        best_sum = -sys.maxsize
        current_sum = 0
        for num in nums:
            current_sum = max(num, current_sum+num)
            best_sum = max(best_sum, current_sum)
        return best_sum
    
    dp = collections.defaultdict(int)
    def climbStairs(self, n:int):
        """
        87. 계단 오르기(leetcode : 70)
        a. 메모이제이션
        """
        if n <= 2:
            return n
        
        if self.dp[n]:
            return self.dp[n]
        self.dp[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.dp[n]
    
    def rob_a(self, nums:List[int]):
        """
        88. 집 도둑(leetcode : 198)
        a. 타뷸레이션
        """
        if not nums:
            return 0
        if len(nums) <= 2:
            return max(nums)
        
        dp = collections.OrderedDict()
        dp[0], dp[1] = nums[0], max(nums[0], nums[1])
        
        for i in range(2, len(nums)):
            dp[i] = max(dp[i-1], dp[i-2] + nums[i])
            
        return dp.popitem()[1]