from typing import List

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

# 연결리스트에서 중앙값을 아는법 : Runner 기법
class Solutuin:
    def mergeTwoList(self, l1: ListNode, l2:ListNode) -> ListNode:
        if l1 or l2:
            if l1.val > l2.val:
                l1, l2 = l2, l1
            l1.next = self.mergeTwoList(l1.next, l2)
        return l1 or l2
    
    def sortList_a(self, head: ListNode) -> ListNode:
        """
        58. 리스트 정렬(leetcode : 148)
        a. 병합 정렬(퀵 정렬(로무토 파티션)->타임아웃)
        """
        if not (head and head.next):
            return head
        
        half, slow, fast = None, head, head
        while fast and fast.next:
            half, slow, fast = slow, slow.next, fast.next.next
        half.next = None
        
        l1 = self.sortList_a(head)
        l2 = self.sortList_a(slow)
        
        return self.mergeTowLists(l1, l2)    
        
    def sortList_b(self, head: ListNode) -> ListNode:
        """
        58. 리스트 정렬(leetcode : 148)
        b. 내장 함수 이용
        """
        p = head
        lst: List = []
        while p:
            lst.append(p.val)
            p = p.next
        
        lst.sort()
        
        p = head
        for i in range(len(lst)):
            p.val = lst[i]
            p = p.next
        return head

    def merge(self, intervals:List[List[int]]) -> List[List[int]]:
        """
        59. 구간 병합(leetcode : 56)
        a. 정렬하여 병합
        """
        merged = []
        for i in sorted(intervals, key = lambda x: x[0]):
            if merged and i[0] <= merged[-1][1]:
                mreged[-1][1] = max(merged[-1][1], i[1])
            else:
                merged += i, # ,(콤마)는 merged + = [i]와 같은 역할, 중첩 리스트로 만들어줌
            
        return merged
    
    def insertSort(self, head:ListNode) -> ListNode:
        """
        60. 삽입 정렬 리스트(leetcode : 147)
        a. 삽입 정렬
        """
        cur = parent = ListNode(0)
        while head:
            while cur.next and cur.next.val < head.val:
                cur = cur.next
            
            cur.next, head.next, head = head, cur.next, head.next
            
            if head and cur.val > head.val:
                cur = parent # 필요한 경우에만 cur 포인터가 처음으로 되돌아가 탐색&비교 
        
        return parent.next
    
    @staticmethod
    def to_swap(n1: int, n2:int)-> bool:
        return str(n1) + str(n2) < str(n1) + str(n2)
    
    def largestNumber(self, nums:List[int]) -> str:
        """
        61. 가장 큰수(leetcode : 179)
        a. 삽입 정렬
        """
        i = 1
        while i < len(nums):
            j = i
            while j > 0 and self.to_swap(nums[j-1], nums[j]):
                nums[j], nums[j-1] = nums[j-1], nums[j]
                j -= 1
            i += 1
        
        return str(int("".join(map(str, nums))))
    
    def sortColors(self, nums:List[int]) -> None:
        """
        63. 색 정렬(leetcode : 75)
        a. 네덜란드 국기 문제 응용
        피벗보다 작은 부분, 같은 부분, 큰 부분 총 세부분으로 분할하는 퀵 정렬
        """
        red, white, blue = 0, 0, len(nums)
        
        while white < blue:
            if nums[white] < 1:
                nums[red], nums[white] = nums[white], nums[red]
                white += 1
                red += 1
            elif nums[white] > 1:
                blue -=1
                nums[white], nums[blue] = nums[blue], nums[white]
            else:
                white += 1
                
    def kClosestPoint(self, points:List[List[int]], K:int) -> List[List[int]]:
        """
        64. 원점에 K번째로 가까운 점
        a. 유클리드 거리의 우선순위큐 순서        
        """
        import heapq
        heap = []
        for (x,y) in points:
            dist = x**2 + y**2
            heapq.heappush(heap, (dist,x,y))
        
        result = []
        for _ in range(K):
            (dist, x, y) = heapq.heappop(heap)
            result.append((x,y))
        return result
    
        