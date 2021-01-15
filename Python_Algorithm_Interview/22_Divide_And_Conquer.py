from typing import List
import collections

class Solution:
    def majorityElement_a(self, nums:List[int])-> int:
        """
        83. 과반수 엘리먼트(leetcode : 169)
        a. 다이나믹 프로그래밍
        """
        counts = collections.defaultdict(int)
        for num in nums:
            if counts[num] == 0:
                counts[num] = nums.count(num)
            
            if counts[num] > len(nums) // 2:
                return num

    def majorityElement_b(self, nums:List[int])-> int:
        """
        83. 과반수 엘리먼트(leetcode : 169)
        b. 분할 정복
        """
        if not nums:
            return None
        if len(nums) == 1:
            return nums[0]
        
        half = len(nums) // 2
        a = self.majorityElement_a(nums[:half])
        b = self.majorityElement_a(nums[half:])
        
        return [b, a][nums.count(a) > half]
        
    def majorityElement_c(self, nums:List[int])-> int:
        """
        83. 과반수 엘리먼트(leetcode : 169)
        c. Pythonic
        """
        return sorted(nums)[len(nums) // 2]
    
    def diffWays(self, input:str) -> List[int]:
        """
        84. 괄호를 삽입하는 여러 가지 방법(leetcode : 241)
        a. 분할 정복
        """
        def compute(left, right, op):
            results = []
            for l in left:
                for r in right:
                    results.append(eval(str(l)+op+str(r)))
            return results
        
        if input.isdigit():
            return [int(input)]
        
        results = []
        for index, value in enumerate(input):
            if value in "-+*":
                left = self.diffWays(input[:index])
                right = self.diffWays(input[index+1:])
                
                results.append(compute(left, right, value))
            
        return results
    