from typing import List
import heapq

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:
    def mergeKLists(self, lists : List[ListNode]) -> ListNode:
        """
        27. k개 정령 리스트 병합(leetcode : 23. Merge k Sorted Lists)
        a. 우선순위 큐를 이용한 리스트 병합
        """
        root = result = ListNode(None)
        heap = []
        
        # 중복된 값이 있을경우 오류 방지를 위해.
        for i in range(len(lists)):
            if lists[i]:
                heapq.heappush(heap, (result.val, i, lists[i]))
        
        while heap:
            node = heapq.heappop(heap) # 가장 작은 노드의 연결 리스트부터 차례대로 나오게 함
            idx = node[1] 
            result.next = node[2]
        
            result = result.next
            if result.next: 
                heapq.heappush(heap, (result.next.val, idx, result.next))
            # k개의 연결 리스트가 항상 힙에 들어가 있어야 
            # 그 중 가장 작은 노드가 차례대록 나올 수 있기 때문에 
            # 힙에 pop된 연결 리스트의 나머지 부분을 push
        return root.next


                 