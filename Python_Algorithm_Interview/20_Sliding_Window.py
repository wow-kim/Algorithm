from typing import List

class Solution:
    def maxSlidingWindow(self, nums:List[int], k:int)-> List[int]:
        """
        75. 최대 슬라이딩 윈도우(leetcode : 239)
        a. 큐를 이용해 부르트 포스 최적화
        필요할 때만 전체의 최대값을 계산하고 
        이외에는 새로 추가되는 값만 기존의 최대값과 비교
        """
        import collections
        
        results = []
        window = collections.deque()
        current_max = float('-inf')
        
        for i,v in enumerate(nums):
            window.append(v)
            if i < k-1:
                continue
            
            if current_max == float("-inf"):
                current_max = max(window)
            elif v > current_max:
                current_max = v
                
            if current_max == window.popleft():
                current_max = float('-inf')
        
        return results
    
    def minWindow(self, s:str,t:str)->str:
        """
        76. 부분 문자열이 포함된 최소 윈도우(leetcode : 76)
        a. 투 포인터, 슬라이딩 윈도우 이용
        """
        import collections
        
        need = collections.Counter(t)
        missing = len(t) # 필요한 문자의 전체 개수
        left = start = end = 0
        
        for right, char in enumerate(s, 1):
            missing -= need[char] > 0
            need[char] -= 1
            
            if missing == 0:
                while left < right and need[s[left]] < 0:
                    need[s[left]] += 1
                    left += 1
                
                if not end or right - left <= end - start:
                    start, end = left, right
                    
                need[s[left]] += 1
                missing += 1
                left += 1
        
        return s[start:end]
    
    print("check")
            
        