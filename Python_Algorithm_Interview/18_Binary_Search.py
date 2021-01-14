from typing import List

class Solution:
    def search_a(self, nums:List[int], target: int) -> int:
        """
        65. 이진 검색
        a. 재귀 풀이
        """
        def binary_search(left, right):
            if left <= right:
                mid = (left + right) // 2

                if nums[mid] < target:
                    return binary_search(mid + 1, right)
                elif nums[mid] > target:
                    return binary_search(left, mid-1)
                else:
                    return mid
            else:
                return -1
        
        return binary_search(0, len(nums)-1)
    
    def search_b(self, nums:List[int], target: int) -> int:
        """
        65. 이진 검색
        b. 반복 풀이
        """
        left, right = 0, len(nums) -1
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] < target:
                left = mid + 1
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
        else:
            return -1
        
    def search_c(self, nums:List[int], target: int) -> int:
        """
        65. 이진 검색
        c. 이진 검색 모듈
        """
        import bisect
        index = bisect.bisect_left(nums, target)
        
        if index < len(nums) and nums[index] == target:
            return index
        else:
            return -1
        
    def searchInRotatedSortedArray(self, nums: List[int], target:int) -> int:
        """
        66. 회전 정렬된 배열 검색
        a. 피벗을 기준으로 한 이진 검색
        피벗을 기준으로 입력값이 돌아간 상황인데, 피벗이 어떤 것인지 모르므로 기존의 이진 검색 활용 불가
        """
        if not nums:
            return -1
        
        left, right = 0, len(nums) -1
        while left <= right: # 최소값 찾아 피벗으로 설정
            mid = left + (right - left) // 2
            
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid
                
        pivot = left
        
        left, right = 0, len(nums)-1
        while left < right:
            mid =left + (right - left) //2
            mid_pivot = (mid + pivot) % len(nums)
            
            if nums[mid_pivot] < target:
                left = mid + 1
            elif nums[mid_pivot] > target:
                right = mid - 1
            else:
                return mid_pivot
            
        return - 1
    
    def intersection_a(self, nums1:List[int], nums2:List[int]) -> List[int]:
        """
        67. 두 배열의 교집합
        a. 이진 검색으로 일치 여부 판별
        한 쪽은 순서대로 탐색 & 다른 한쪽은 정렬 후 이진 검색으로 찾기
        시간 복잡도 : O(n logn)
        """
        import bisect
        
        result:Set = set()
        nums2.sort()
        for n1 in nums1:
            i2 = bisect.bisect_left(nums2, n1)
            if len(nums2) > 0 and len(nums2) > i2 and n1 == nums2[i2]:
                result.add(n1)
        
        return result
    
    def intersection_b(self, nums1:List[int], nums2:List[int]) -> List[int]:
        """
        67. 두 배열의 교집합
        b. 투 포인터로 일치 여부 판별
        시간 복잡도 : O(n)
        """
        result:Set = set()
        nums1.sort()
        nums2.sort()
        i = j = 0
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                result.add(nums1[i])
                i += 1
                j += 1
        
        return result
    
    def twoSum_a(self, numbers:List[int], target:int) -> List[int]:
        """
        68. 두 수의 합
        a. 투 포인터
        """
        left, right = 0, len(numbers) -1
        while not left == right:
            if numbers[left] + numbers[right] < target:
                left += 1
            elif numbers[left] + numbers[right] > target:
                right -= 1
            else:
                return left + 1, right + 1

    def twoSum_b(self, numbers:List[int], target:int) -> List[int]:
        """
        68. 두 수의 합
        b. 이진 검색
        """
        for k, v in enumerate(numbers):
            left, right = k + 1, len(numbers) - 1
            expected = target - v
            
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] < expected:
                    left = mid + 1
                elif numbers[mid] > expected:
                    right = mid - 1
                else:
                    return k + 1, mid + 1

    def twoSum_c(self, numbers:List[int], target:int) -> List[int]:
        """
        68. 두 수의 합
        c. bisect 모듈 사용
        """
        import bisect
        for k, v in enumerate(numbers):
            expected = target - v
            i = bisect.bisect_left(numbers, expected, k+1)
            if i < len(numbers) and numbers[i] == expected:
                return k + 1, i + 1
            
    def searchMatrix_a(self, matrix, target):
        """
        69. 2D 행렬 검색 2
        a. 첫 행의 맨 뒤에서 탐색
        """
        if not matrix:
            return False
        
        row = 0
        col = len(matrix[0]) - 1
        
        while row <= len(matrix) and col >= 0:
            if target == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            elif target > matrix[row][col]:
                row += 1
        return False
    
    def searchMatrix_b(self, matrix, target):
        """
        69. 2D 행렬 검색 2
        b. Pythonic
        """
        return any(target in row for row in matrix)
                            
            
    
