from typing import List
import heapq

class Solution:
    def findKth_a(self, nums:List[int], k:int) -> int:
        """
        55. 배열의 K번째 큰 요소
        a. heapq 모듈 이용
        """
        heapq.heapify(nums)
            
        for _ in range(len(nums)-k):
            heapq.heappop(nums)
        
        return -heapq.heappop(nums)
    
    def findKth_b(self, nums:List[int], k:int) -> int:
        """
        55. 배열의 K번째 큰 요소
        b. heaqp 모듈의 nlargest 이용
        """
        return heapq.nlargest(k, nums)[-1]
    