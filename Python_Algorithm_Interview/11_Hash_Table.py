from typing import List
import collections
# 해시 테이블의 가장 큰 특징은 대부분의 연산이 시간 복잡도가 O(1)이라는 것입니다..
class ListNode:
    def __init__(self, key= None, value=None):
        self.key = key
        self.value = value
        self.next = None

class HashMap:
    '''
    28. 해쉬맵 디자인(leetcode : 706. Design HashMap)
    해쉬 맵 구현
    개별 체이닝 방식으로
    '''
    def __init__(self):
        self.size = 1000 # 기본 사이즈 : 1000
        self.table = collections.defaultdict(ListNode) # 존재하지 않는 키를 조회하면 default를 생성
        
    def put(self, key: int , value: int ) -> None:
        index = key % self.size # Modulo-Division Method
        
        # 존재하지 않는 인덱스를 조회할 경우 에러를 생성하지 않고 defaultdict에 의해 빈 ListNode 생성
        if self.table[index].value is None: 
            self.table[index] = ListNode(key, value)
            return
        
        p = self.table[index] # 인덱스가 존재하는 경우
        while p:
            if p.key == key:
                p.value = value
                return
            if p.next is None: 
                break
            p = p.next
            
        p.next = ListNode(key, value) # chaining
       
    def get(self, key: int) -> int:
        index = key % self.size
        if self.table[index].value is None: # 인덱스에 아무것도 없으면(빈 노드도 없으면) -1 반환
            return -1
        
        p = self.table[index]
        while p:
            if p.key == key:
                return p.value
            p = p.next
        return -1 # 노드는 존재하지만 값이 존재 하지 않는 경우        
                
    def remove(self, key: int) -> None:
        index = key % self.size
        if self.table[index].value is None: # 아무것도 존재하지 않는 경우 그냥 return
            return
        
        # 인덱스의 첫번째 노드일 경우
        p = self.table[index]
        if p.key == key:
            self.table[index] = ListNode() if p.next is None else p.next
            return
        
        # 연결리스트의 노드 삭제
        prev = p
        while p:
            if p.key == key:
                prev.next = p.next # 첫번째 노드일 경우를 예외처리 해주는 이유
                return
            prev, p = p, p.next
    
class Solution:
    def JewelsStones_a(self, J: str, S:str) -> int:
        '''
        29. 보석과 돌(leetcode : 771. Jewels and Stones)
        a. defaultdict를 이용해 비교를 생략한 해쉬 테이블 풀이, 처음 등장하는 경우를 위해
        '''
        freqs = collections.defaultdict(int)
        count = 0
        
        for char in S:
            freqs[char] += 1
        
        for char in J:
            count += freqs[char]
            
        return count
    
    def JewelsStones_c(self, J: str, S:str) -> int:
        '''
        29. 보석과 돌(leetcode : 771. Jewels and Stones)
        c. Counter 사용
        '''
        freqs = collections.Counter(S)
        count = 0 
        
        for char in J:
            count += freqs[char]
        
        return count
    
    def JewelsStones_d(self, J: str, S:str) -> int:
        '''
        29. 보석과 돌(leetcode : 771. Jewels and Stones)
        d. Pythonic, 리스트 컴프리헨션
        '''
        return sum(s in J for s in S)
    
    def LongestSubstring(self, s: str) -> int:
        '''
        30. 중복 문자 없는 가장 긴 문자열
        a. 슬라이딩 윈도우 & 투 포인터
        '''
        used = {}
        max_length = start = 0
        
        for index, char in enumerate(s):
            if char in used and start <= used[char]:
                start = used[char] + 1 # 이미 등장했다면 start 포인터 위치 갱신
            else:
                max_length = max(max_length, index - start + 1)
            
            used[char] = index        
        
        return max_length