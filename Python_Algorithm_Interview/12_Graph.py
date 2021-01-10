from typing import List
import itertools
import collections

class SolutionL:
    def numIsland(self, grid: List[List[str]]) -> int:
        """
        32. 섬의 개수(leetcode : 200. Number of Island)
        a. dfs로 그래프 탐색
        """
        def dfs(i, j): # numIsland 내에 중첩함수로
            if i < 0 or i >= len(grid) or \
                j < 0 or j >= len(grid[0]) or \
                    grid[i][j] != "1":
                        return
            
            grid[i][j] = 0 # 이미 방문한 곳은 1이 아닌 값으로 마킹
            
            dfs(i+1, j)
            dfs(i-1, j)
            dfs(i, j+1)
            dfs(i, j-1)
            
        count = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs[i,j]
                    
                    count += 1
        return count


    def LetterCombination(self, digits:str) -> List[str]:
        """
        33. 전화 번호 문자 조합(leetcode : 17. Letter Combination of a Phone Number)
        a. 모든 조합 탐색
        """
        def dfs(index, path):
            if len(path) == len(digits):
                result.append(path)
                return
            
            for i in range(index, len(digits)):
                for j in dic[digits[i]]:
                    dfs(i+1, path + j)
            
        if not digits:
            return []
        
        dic = {"2":"abc", "3":"def", "4":"ghi", "5":"jkl",
               "6":"mno", "7":"pqrs", "8":"tuv","9":"wxyz"}
        result = 0
        dfs(0, "")
        
        return result 
    
    def Permutation_a(self, nums:List[int]) -> List[List[int]]:
        """
        34. 순열(leetcode : 46. Permutation)
        a. DFS를 활용
        """
        results = []
        prev_elements = []
        
        def dfs(elements):
            if len(elements) == 0:
                results.append(prev_elements[:]) # 참조를 append하는게 아닌 값을 append 해야하므로 [:]
            
            for e in elements:
                next_elements = elements[:]
                next_elements.remove(e)
                
                prev_elements.append(e)
                dfs(next_elements)
                prev_elements.pop(0)
            
        dfs(nums)
        return results                
    
    def Permutation_b(self, nums:List[int]) -> List[List[int]]:
        """
        34. 순열(leetcode : 46. Permutation)
        b. itertools 활용
        """
        return list(itertools.permutations(nums)) # 튜플로 반환하기 때문에 list() 사용
    
    def Combination_a(self, n:int, k:int) -> List[List[int]]:
        """
        35. 조합(leetcode : 77. Combination)
        a. dfs로 k개 조합 생성
        """
        results = []
        
        def dfs(elements, start:int, k:int):
            if k ==0:
                results.append(elements[:])
            
            for i in range(start, n+1):
                elements.append(i)
                dfs(elements, i+1, k-1)
                elements.pop()

        dfs([], 1, k)
        return results
    
    def Combination_b(self, n:int, k:int) -> List[List[int]]:
        """
        35. 조합(leetcode : 77. Combination)
        b. itertools 사용
        """
        return list(itertools.combinations(range(1,n+1),k))
    
    def CombinationSum(self, candidates:List[int], target: int) -> List[int]:
        '''
        36. 조합의 합(leetcode : 39. Combination Sum)
        a. DFS로 중복 조합 그래프 탐색
        '''
        result = []
        
        def dfs(csum, index, path):
            if csum < 0:
                return
            if csum == 0:
                result.append(path)
                return
            
            for i in range(index, len(candidates)):
                dfs(csum - candidates[i], i, path+[candidates[i]])
        
        dfs(target, 0, [])
        return result        
    
    def Subsets(self, nums:List[int]) -> List[List[int]]:
        """
        37. 부분 집합(leetcode : 78. Subsets)
        a. 트리의 모든 DFS 결과
        """
        result = []
        
        def dfs(index, path):
            result.append(path) # 모든 탐색이 정답(subset)
            
            for i in range(index, len(nums)):
                dfs(i+1, path + [nums[i]])
        
        dfs(0, [])
        return result
    
    def Reconstruct_a(self, tickets:List[List[str]]) -> List[str]:
        """
        38. 일정 재구성(leetcode : 332. Reconstruct Itinerary)
        a. DFS로 그래프 구성
        "JFK"에서 출발하는 여행 일정, 사전 어휘 순으로 방문
        """
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop(0))
            route.append(a)
            
        dfs("JFK")
        return route[::-1]
    
    def Reconstruct_b(self, tickets:List[List[str]]) -> List[str]:
        """
        38. 일정 재구성(leetcode : 332. Reconstruct Itinerary)
        b. 스택 연산으로 큐 연산 최적화 시도
        "JFK"에서 출발하는 여행 일정, 사전 어휘 순으로 방문
        """
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets, reverse=True):
            graph[a].append(b)
        
        route = []
        def dfs(a):
            while graph[a]:
                dfs(graph[a].pop()) # pop(0)은 O(n), pop()은 O(1)
            route.append(a)
            
        dfs("JFK")
        return route[::-1]
    
    def Reconstruct_c(self, tickets:List[List[str]]) -> List[str]:
        """
        38. 일정 재구성(leetcode : 332. Reconstruct Itinerary)
        c. 일정 그래프 반복
        "JFK"에서 출발하는 여행 일정, 사전 어휘 순으로 방문
        """
        graph = collections.defaultdict(list)
        for a, b in sorted(tickets):
            graph[a].append(b)
            
        route, stack = [], ['JFK']
        while stack:
            while graph[stack[-1]]:
                stack.append(graph[stack[-1]].pop(0))
            route.append(stack.pop()) # 막히는 부분에서 풀어내도록 처리
        
        return route[::-1]
    
    def CourseSchedule_a(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        39. 코스 스케쥴(leetcode : 207. Course Schedule)
        a. DFS로 순환 구조 판별, 순환 구조라면 계속 맴돌게 될 것입니다.
        이전에 방문했던 노드를 또 방문하게 된다면 순환구조(False)
        """
        graph = collections.defaultdict(list)
        for x, y in prerequisites:
            graph[x].append(y)
        
        traced = set()
        
        def dfs(i):
            if i in traced:
                return False
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            traced.remove(i)
            
            return True
        
        for x in list(graph):
            if not dfs(x):
                return False
        
        return True
    
    def CourseSchedule_b(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        """
        39. 코스 스케쥴(leetcode : 207. Course Schedule)
        b. 가지치기를 이용한 최적화
        이전에 방문했던 노드를 또 방문하게 된다면 순환구조(False)
        """
        graph = collections.defaultdict(list)
        for x,y in prerequisites:
            graph[x].append(y)
        
        visited = set() # 한 번 방문했던 그래프는 무조건 True를 반환하도록 
        traced = set()
        
        def dfs(i):
            if i in traced:
                return False
            
            if i in visited:
                return True
            
            traced.add(i)
            for y in graph[i]:
                if not dfs(y):
                    return False
            
            traced.remove(i)
            
            visited.add(i)
            
            return True
        
        for x in list(graph): #새로운 복사본을 생성, RuntimeError 방지(graph 값이 변경될때)
            if not dfs(x):
                return False
        
        return True
    