from typing import List

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

# last -> 3 -> 2 -> 1 -> None    
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)

for _ in range(3):
    print(stack.pop())
    
# 파이썬에서는 동적 배열인 list자료형으로 stack, que를 쉽게 구현할 수 있다.
# 속도는 더 느릴수도?

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