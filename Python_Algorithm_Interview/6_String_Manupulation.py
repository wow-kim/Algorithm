from typing import List

class Solution:
    
    def q1_a(self, s:str) -> bool:
        ''' 
        01. 유효한 팰린드롬 
        a. Deque 자료형을 이용한 최적화
        '''
        import collections
        
        strs:Deque = collections.deque()
        
        for char in s:
            if char.isalnum():
                strs.append(char.lower())
        
        while len(strs) > 1:
            if strs.popleft() != strs.pop:
                return False
        
        return True
    
    def q1_b(self, s: str) -> bool:
        ''' 
        01. 유효한 팰린드롬 
        b. 정규표현식, 슬라이싱 사용
        '''
        import re
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)
        
        return s == s[::-1]
    
    def q2_a(self, s: List[str]) -> None:
        '''
        02. 문자열 뒤집기
        a. 투 포인터를 이용한 스왑
        '''
        left, right = 0, len(s)-1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1
    
    def q3_a(self, logs:List[str]) -> List[str]:
        """
        03. 로그 파일 재정렬
        a. 람다와 + 연산자 
        """
        letters, digits = [], []
        for log in logs:
            if log.split()[1].isdigit():
                digits.append(log)
            else:
                letters.append(log)
        
        letters.sort(key = lambda x: (x.split()[1], x.split()[0]))
        return letters + digits
    
    def q4_a(self, paragraph:List[str], banned:List[str]) -> List[str]:
        """
        04. 가장 흔한 단어
        a. 리스트 컴프리헨션, Counter 객체 사용
        """
        import re
        import collections
        words = [word for word in re.sub(r"[^\w]"," ",paragraph) # 단어 문자가 아닌 모든 문자를 공백으로 치환
                 .lower().split() if word not in banned] 
        
        counts = collections.Counter(words)
        return counts.most_common(1)[0][0]
    
    def q5_a(self, strs:List[str]) -> List[str]:
        """
        05. 그룹 애너그램
        a. 정렬하여 딕셔너리에 추가
        """
        import collections
        
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams["".join(sorted(word))].append(word)
        
        return anagrams.values()
    
    def q6_a(self, s:str) -> str:
        """
        06. 가장 긴 팰린드롬 부분 문자열
        a. 중앙을 중심으로 확장하는 풀이
        """
        
        # 예외 처리
        if len(s) < 2 or s==s[::-1]:
            return s
        
        def expand(left: int, right:int) -> str:
            while left >= 0 and right <= len(s) and s[left] == s[right-1]:
                left -=1
                right +=1
            return s[left+1:right-1]
        
        result = ""
        for i in range(len(s)-1):
            result = max(result, expand(i,i+1), expand(i,i+2), key = len)
        
        return result

answer = Solution()
print(answer.q1_a("race a car"))