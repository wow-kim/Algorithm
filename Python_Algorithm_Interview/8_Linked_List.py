from typing import List

# 연결 리스트(Linked List)는 배열과 달리 특정 인덱스에 접근하기 위해서 
# # 전체를 순서대로 읽어야 하므로 상수 시간에 접근할 수 없다. -> O(n)

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class Solution:  
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
            if q.pop(0) != q.pop(): # pop(0) 함수의 경우 첫 번째 값을 꺼내오면 모든 값이 한칸 씩 shifting되어 O(n) 발생
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
    
    def q1_c(self, head:ListNode) -> bool:
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

    # 연결리스트를 뒤집는 문제는 매우 일반적이면서 활용도가 높은 문제로, 실무에서도 빈번하게 쓰입니다.
    # 재귀, 반복 두가지 방법으로 해결해보겠습니다.
    def reverselist_a(self, head:ListNode) -> ListNode:
        '''
        15. 역순 연결 리스트(leetcode : 206. Reverse Linked List)
        a. 재귀 구조
        '''
        def reverse(self, node:ListNode, prev:ListNode = None):
            if not node:
                return prev
            next, node.next = node.next, prev
            return reverse(next, node)        

        return reverse(head)
    
    def reverselist_b(self, head:ListNode) -> ListNode:
        '''
        15. 역순 연결 리스트(leetcode : 206. Reverse Linked List)
        b. 반복 구조
        '''
        node, prev = head, None
        
        while node:
            next, node.next = node.next, prev
            prev, node = node, next     
            
        return prev
    
    def addTwoNumbers(self, l1:ListNode, l2:ListNode) -> ListNode:
        '''
        16. 두 수의 덧셈(leetcod : 2. Add Two Numbers)
        a. 전가산기 구현
        '''
        root = head = ListNode(0)
        
        carry = 0
        while l1 or l2 or carry:
            sum = 0
            if l1:
                sum += l1.val
                l1 = l1.next
            if l2:
                sum += l2.val
                l2 = l2.next

            carry, val = divmod(sum+carry, 10) #몫 carry는 자리 올림수로 설정해 다음자릿수의 연산에 사용됩니다.
            head.next = ListNode(val)
            head = head.next

        return root.next #head와 동시에 할당한 root에도 연결됩니다. 이렇게 해주는 이유는 head의 포인터가 이미 전진해버렸기 때문입니다.(제 생각)

    def swapPairs_a(self, head: ListNode) -> ListNode:
        '''
        17. 페어의 노드 스왑
        a. 반복 구조로 스왑
        '''
        root = prev = ListNode(None)
        prev.next = head
        
        while head and head.next:
            b = head.next
            head.next = b.next
            b.next = head
            
            prev.next = b
            
            head = head.next
            prev = prev.next.next
            
        return root.next
    
    def swapPairs_b(self, head: ListNode) -> ListNode:
        '''
        17. 페어의 노드 스왑
        b. 재귀 구조로 스왑
        '''
        if head and head.next:
            p = head.next
            
            head.next = self.swapPairs_b(p.next) # 한번에 두칸씩(next가 두번이니까)
            p.next = head
            return p # 백트래킹
        
        return head
                
    def oddEvenList(self, head: LisNode) -> ListNode:
        '''
        18. 홀짝 연결 리스트(leetcode : 328. Odd Even Linked List)
        a. 반복 구조로 홀짝 노드 처리
        홀 노드, 짝 노드를 각각 구성한 다음에 홀수 노드의 마지막과 짝수 노드의 처음을 이어줍니다.
        '''
        if head is None:
            return None
        
        odd = head #개체 복사
        even = head.next
        even_head = head.next
        
        while even and even.next:
            odd.next, even.next = odd.next.next, even.next.next
            odd, even = odd.next, even.next
        
        odd.next = even_head
        
        return head 

    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        '''
        19. 역순 연결 리스트 2(leetcode : 92. Reverse Linked List 2)
        a. 반복 구조로 노드 뒤집기
        '''
        if not head or m == n:
            return head
        
        root = start = ListNode(None)
        root.next = head
        for _ in range(m-1):
            start = start.next # start는 m번째 node직전,
        end = start.next # end는 m번째 node에
        
        for _ in range(n-m):
            tmp, start.next, end.next = start.next, end.next, end.next.next
            start.next.next = tmp
        return root.next
        
llist1 = ListNode(2)
llist1.next = ListNode(4)
llist1.next.next = ListNode(3)

llist2 = ListNode(5)
llist2.next = ListNode(6)
llist2.next.next = ListNode(4)

sol = Solution()
print(sol.addTwoNumbers(llist1, llist2).val)
