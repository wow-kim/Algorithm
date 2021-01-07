from typing import List

class Solution:
    
    # 입력값인 nums가 정렬된 상태가 아니므로 투 포인터를 쓸 수 없습니다.
    # 임의로 정렬하게 되면 인덱스가 엉망이 되어 문제가 발생합니다.
    # 인덱스가 아닌 값을 찾는 문제라면 투 포인터로 해결이 가능합니다.
    
    def q1_a(self, nums:List[int], target:int) -> List[int]:
        '''
        07. 두 수의 합(leetcode : 1. Two Sum)
        a. in을 이용한 탐색
            시간복잡도 : O(n^2)
        '''
        for i, n in enumerate(nums):
            complement = target - n
            if complement in nums[i+1]:
                return nums.index(n), nums[i+1:].index(complement) + (i+1)
            
    def q1_b(self, nums:List[int], target:int) -> List[int]:
        '''
        07. 두 수의 합(leetcode : 1. Two Sum)
        b. 첫 번째 수를 뺀 결과 키 조회
            딕셔너리는 해시 테이블로 구현되어 있어, 평균적으로 O(1)에 조회가 가능합니다.
            시간복잡도 : O(n)
        '''
        nums_map = {}
        for i, num in enumerate(nums):
            nums_map[num] = i
        
        for i, num in enumerate(num):
            if target - num in nums_map and i != nums_map[target-num]:
                return nums.index(num), nums_map[target - num]
    
    def q1_c(self, nums:List[int], target:int) -> List[int]:
        '''
        07. 두 수의 합(leetcode : 1. Two Sum)
        c. q1_b의 조회 구조 개선
            시간복잡도 : O(n)
        '''
        nums_map = {}
        for i, num in enumerate(nums):
            if target - num in nums_map:
                return [nums_map[target-num], i]
            nums_map[num] = i
            
    
    def q2_a(self, height:List[int]) -> int:
        '''
        08. 빗물 트래핑(leetcode : 42. Trapping Rain Water)
        a. 투 포인터를 최대로 이동
            시간 복잡도 : O(n)
        '''
        if not height: 
            return 0
        
        # 두 개의 포인터(left, right)가 가장 높은 막대를 향해 이동
        volume = 0
        left, right = 0, len(height)-1
        left_max, right_max = height[left], height[right]
        
        while left < right:
            left_max, right_max = max(height[left], left_max), max(height[right], right_max)
            
            if left_max <= right_max:
                volume += left_max - height[left]
                left += 1
            else:
                volume += right_max - height[right]
                right -= 1
        return volume
    
    def q2_b(self, height: List[int]) -> int:
        '''
        08. 빗물 트래핑(leetcode : 42. Trapping Rain Water)
        b. 스택 쌓기
            시간 복잡도 : O(n)
        '''
        
        stack = []
        volume = 0
        
        for i in range(len(height)):
            
            while stack and height[i] > height[stack[-1]]:
                top = stack.pop()
                
                if not len(stack):
                    break
                
                distance = i - stack[-1] -1
                waters = min(height[i], height[stack[-1]]) - height[top]
                
                volume += distance * waters
            
            stack.append(i)
        
        return volume

    def q3_a(self, nums:List[int]) -> List[List[int]]:
        '''
        09. 세 수의 합(leetcode : 15. 3Sum)
        a. 투 포인터로 합 계산
            시간 복잡도 : O(n^2)
        '''
        results = []
        nums.sort()
        
        for i in range(len(nums)-2):
            
            # 중복 값 건너뛰기
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            left, right = i+1, len(nums)-1
            while left < right:
                sum = nums[i] + nums[left] + nums[right]
                if sum < 0:
                    left += 1
                elif sum >0:
                    right -= 1
                else:
                    results.append([nums[i], nums[left], nums[right]])
                    
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right -1]:
                        right +=1
                    left += 1
                    right -= 1
        
        return results
    
    def q4_a(self, nums : List[int]) -> int:
        '''
        10. 배열 파티션 1(leetcode : 561. Array Partition 1)
        a. Pythonic Way
        '''
        # 슬라이싱 [::2]는 2칸씩 건너 뛰게합니다.
        return sum(sorted(nums)[::2])
                    
    def q5_a(self, nums: List[int]) -> List[int]:
        '''
        11. 자신을 제외한 배열의 곱(leetcode : 238. Product of Array Except Self)
        a. 왼쪽 곱셉 X 오른쪽 곱셈
        '''
        out = []
        
        p=1
        for i in range(0,len(nums)):
            out.append(p)
            p = p*nums[i]
        
        p = 1
        for i in range(len(nums)-1, 0 - 1, -1):
            out[i] = out[i]*p
            p = p*nums[i]
        
        return out

    def q6_a(self,prices:List[int]) -> int:
        '''
        12. 주식을 사고팔기 가장 좋은 시점(leetcode : 121. Best Time to Buy and Sell Stock)
            한 번의 거래로 낼 수 있는 최대 이익 산출
        a. 저점과 현재 값과의 차이 계산(카데인 알고리즘 응용)
        '''
        profit = 0
        min_price = float("inf")
        # 최대값과 최소값의 초기값을 지정해주는 방법 : 
        # 최초 비교에서 반드시 다른 값으로 대체되도록 해주어야 합니다.
        
        for price in prices:
            min_price = min(min_price, price)
            profit = max(profit, price-min_price)
        
        return profit
        
ans = Solution()
print(ans.q5_a([1,2,3,4]))