from typing import List

class solution:
    def maxProfit_a(self, prices:List[int]) -> int:
        """
        78. 주식을 사고팔기 가장 좋은 시점 2(leetcode : 122)
        a. 그리디 알고리즘
        """
        result = 0
        for i in range(len(prices)-1):
            if prices[i+1] > prices:
                result += prices[i+1]-prices[i]
        return result
    
    def maxProfit_b(self, prices:List[int]) -> int:
        """
        78. 주식을 사고팔기 가장 좋은 시점 2(leetcode : 122)
        b. Pythonic
        차이가 0 이상이면 무조건 더하기
        """
        return sum(max(prices[i+1]-prices[i], 0) for i in range(len(prices) -1))
    
    def reconstructQueue(self, people: List[List[int]]) -> List[List[int]]:
        """
        79. 키에 따른 대기열 재구성(leetcode : 406)
        a. 우선순위 큐 사용
        """
        import heapq
        heap = []
        for person in people:
            heapq.heappush(heap, (-person[0], person[1]))
        
        result = []
        while heap:
            person = heapq.heappop(heap)
            result.insert(person[1], [-person[0], person[1]])
        return result 
    
    def leastInterval(self, tasks : List[str], n:int)->int:
        """
        80. 태스크 스케쥴러(leecode : 621)
        a. 우선순위 큐 사용
        """
        import collections
        import heapq
        counter = collections.Counter()
        result = 0
        
        while True:
            sub_count = 0
        
            for task, _ in counter.most_common(n+1): #큰 순서대로 출력(not 추출)
                sub_count += 1
                result += 1
            
                counter.subtract(task) # 추출이 아니기 때문에 count 줄여줌
                counter += collections.Counter() # 0 이하인 아이템들 제거
                
            if not counter:
                break
            
            result += n - sub_count + 1
        
        return result

    def completeCircuit(self, gas:List[int], cost:List[int])->int:
        """
        81. 주유소(leetcode : 134)
        a. 한 번 방문
        """
        if sum(gas) < sum(cost):
            return -1
        
        start, fuel = 0, 0
        for i in range(len(gas)):
            if gas[i] + fuel < cost[i]:
                start = i + 1
                fuel = 0
            else:
                fuel += gas[i] - cost[i]
        
        return start    
    
    def cookie_a(self, g:List[int], s:List[int]) -> int:
        """
        82. 쿠키 부여(leetcode : 455)
        a. 그리디 알고리즘
        """
        g.sort()
        s.sort()
        
        child_i = cookie_j = 0
        while child_i < len(g) and cookie_j < len(s):
            if s[cookie_j] >= g[child_i]:
                child_i += 1
            cookie_j += 1
            
        return child_i

    def cookie_b(self, g:List[int], s:List[int]) -> int:
        """
        82. 쿠키 부여(leetcode : 455)
        b. 이진 검색
        """
        import bisect
        
        g.sort()
        s.sort()
        
        result = 0
        for i in s:
            index = bisect.bisect_right(g, i)
            if index > result:
                result += 1
                
        return result