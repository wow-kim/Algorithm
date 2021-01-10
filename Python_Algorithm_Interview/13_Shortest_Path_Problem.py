from typing import List
import collections
from collections import heapq

class solution:
    def networkDelayTime(self, times:List[List[int]], N: int, K: int) -> int:
        """
        40. 네트워크 딜레이 타임(leetcode : 743. Network Delay Time)
        a. 다익스트라 알고리즘 구현
        """
        graph = collections.defaultdict(list)
        for u, v, w in times:
            graph[u].append((v,w))
        
        Q = [(0, K)] # (소요 시간, 노드)
        dist = collections.defaultdict(int)
        
        while Q:
            time, node = heapq.heappop(Q)
            if node not in dist:
                dist[node] = time
                for v, w in graph[node]:
                    alt = time + w
                    heapq.heappush(Q, (alt, v))
        
        if len(dist) == N:
            return max(dist.values())
        
        return -1
    
    def CheapestFlight(self, n:int, flights: List[List[int]], src:int, dst:int, K:int) -> int:
        '''
        41. K 경유지 내 가장 저렴한 항공권(leetcode : 787. Cheapest Flights Within K Stops)
        a. 다익스트라 알고리즘 응용
        40번 문제의 코드를 살짝 수정.        
        '''
        graph = collections.defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v,w))
        
        k = 0
        Q = [(0, src , K)] # (비용, 노드, 최대 경유횟수 - 경유횟수)
        
        while Q:
            price, node = heapq.heappop(Q)
            if node == dst:
                return price
            if k >= 0 :                    
                for v, w in graph[node]:
                    alt = price + w
                    heapq.heappush(Q, (alt, v, k-1))
        
        return -1