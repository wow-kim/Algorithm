from typing import List
import collections

# 연결 리스트를 이용한 스택 구현
class Node:
    def __init__(self, item, next):
        self.item = item
        self.next = next
        
class Stack:
    def __init__(self):
        self.last = None
    
    def push(self, item):
        self.last = Node(item, self.last)
    
    def pop(self):
        item = self.last.item
        self.last = self.last.next
        return item

## last -> 3 -> 2 -> 1 -> None    
# stack = Stack()
# stack.push(1)
# stack.push(2)
# stack.push(3)
# 
# for _ in range(3):
#     print(stack.pop())
    
## 파이썬에서는 동적 배열인 list자료형으로 stack, que를 쉽게 구현할 수 있다.
## 속도는 더 느릴수도?

class Solution:
    
    def isValid(self, s:str) -> bool:
        '''
        20. 유효한 괄호(leetcode : 20. Valid Parantheses)
        a. 스택 일치 여부 판별
        '''
        stack = []
        table = {
            ')':'(',
            '}':'{',
            ']':'[' 
        }
        
        for char in s:
            if char not in table: # 딕셔너리에서의 not in
                stack.append(char)
            elif not stack or table[char] != stack.pop():
                return False
        return len(stack) == 0
    
    def removeDuplicateLetters_a(self, s: str) -> str:
        '''
        21. 중복 문자 제거[사전식 나열](leetcod : 316. Remove Duplicate Letters)
        a. 재귀
        '''
        for char in sorted(set(s)):
            suffix = s[s.index(char):]
            
            if set(s) == set(suffix):
                return char + self.removeDuplicateLetters(suffix.replae(char, ''))
        return ''
    
    def removeDuplicateLetters_b(self, s: str) -> str:
        '''
        21. 중복 문자 제거[사전식 나열](leetcod : 316. Remove Duplicate Letters)
        b. 스택
        '''
        counter, seen, stack = collections.Counter(s), set(), []
        
        for char in s:
            counter[char] -= 1
            
            if char in seen:
                continue
            
            while stack and char < stack[-1] and counter[stack[-1]] > 0:
                seen.remove(stack.pop())
            stack.append(char)
            seen.append(char)
            
        return "".join(stack)
    
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''
        22. 일일 온도(leetcod : 739. Daily Temperatures)
        a. 스택 값 비교
        '''
        answer = [0] * len(T)
        stack = []
        for i, cur in enumerate(T):
            while stack and cur > T[stack[-1]]:
                last = stack.pop()
                answer[last] = i-last
            stack.append(i)
        
        return answer
    
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        '''
        23. 큐를 이용해 스택 구현(leetcod : 739. Daily Temperatures)
        a. 스택 값 비교
        '''
        return None