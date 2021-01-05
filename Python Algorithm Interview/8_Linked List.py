from typing import List

class Solution:
    
    # 연결 리스트(Linked List)는 배열과 달리 특정 인덱스에 접근하기 위해서 
    # 전체를 순서대로 읽어야 하므로 상수 시간에 접근할 수 없다. -> O(n)
        
    def q1_a(self, head:ListNode) -> bool:
        '''
        13. 팰린드롬 연결 리스트(leetcode : 234. Palindrome Linked List)
        a. 리스트 변환(pop 함수 이용)
        '''
        q : List = []
        
        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
            
        while len(q) > 1:
            if q.pop(0) != q.pop(0): # pop(0) 함수의 경우 첫 번째 값을 꺼내오면 모든 값이 한칸 씩 shifting되어 O(n) 발생
                return False
        
        return True
    
    def q1_b(self, head:ListNode) -> bool:
        '''
        13. 팰린드롬 연결 리스트(leetcode : 234. Palindrome Linked List)
        b. 데크를 이용한 최적화
        '''
        from collections import deque
        
        q : Deque = deque()
        
        if not head:
            return True
        
        node = head
        while node is not None:
            q.append(node.val)
            node = node.next
        
        while len(q) > 1:
            if q.popleft() != q.pop():
                return False
        
        return True
    
    def q1_c(self, head:LinkeNode) -> bool:
        '''
        13. 팰린드롬 연결 리스트(leetcode : 234. Palindrome Linked List)
        c. 런너(Runner) 기법 활용 : 연결 리스트를 순회할 때 2개의 포인터를 동시에 사용하는 기법입니다.
        한 포인터가 다른 포인터보다 앞서게 하여 병합 지점이나, 중간 위치, 길이 등을 판별할 때 유용하게 사용할 수 있다.
        '''
        rev = None #slow의 역순 연결 리스트를 만들기 위함
        slow = fast = head
    
        while fast and fast.next:
            fast = fast.next.next
            rev, rev.next, slow = slow, rev, slow.next
        
        if fast:
            slow = slow.next
            
        while rev and rev.val == slow.val:
            slow, rev = slow.next, rev.next
        
        return not rev
    
    def q2_a(self, l1:ListNode, l2:ListNode) -> ListNode:
        '''
        14. 두 정렬 리스트의 병합(leetcode : 21. Merge Two Sorted Lists)
        a. 재귀 구조로 연결
        '''
        if (not l1) or (l2 and l1.val > l2.val):
            l1, l2 = l2, l1
        if l1:
            l1.next = self.q2_a(l1.next, l2)
        return l1
