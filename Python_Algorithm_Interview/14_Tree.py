from typing import List
import collections
import sys

class TreeNode: # 이진 트리
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxDepth(self, root:TreeNode) -> int:
        """
        42. 이진 트리의 최대 깊이(leetcode : Maximum Depth of Binary Tree)
        a. 반복 구조로 BFS(너비 우선 탐색) 풀이
        """
        if root is None:
            return 0
        queue = collections.deque([root])
        depth = 0
        
        while queue:
            depth += 1
            for _ in range(len(queue)):
                cur_root = queue.popleft()
                if cur_root.left:
                    queue.append(cur_root.left)
                
                if cur_root.right:
                    queue.append(cur_root.child)
        
        return depth
    
    longest: int = 0
    def diameter(self, root:TreeNode) -> int:
        """
        43. 이진 트리의 직경(leetcode : 543. Diameter of Binary Tree)
        두 노드 간 가장 긴 경로의 길이를 출력
        a. 상태값 누적 트리 DFS
        """
        def dfs(node: TreeNode) -> int:
            if not node:
                return -1
            left = dfs(node.left)
            right = dfs(node.right)
            
            self.longest = max(self.longest, left + right+2) # 가장 긴 경로 갱신
            
            return max(left, right) + 1 # 상태값
        
        dfs(root)
        return self.longest

    result: int = 0
    def longestUnivaluePath(self, root:TreeNode) -> int:
        """
        44. 가장 긴 동일 값의 경로
        a. 상태값 거리 계산 DFS
        """
        def dfs(node: TreeNode):
            if node is None:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)
            
            if node.left and node.left.val == node.val:
                left += 1
            else:
                left = 0
            if node.right and node.right.val == node.val:
                right += 1
            else:
                right = 0
            
            result = max(result, left+right)
            
            return max(left, right)
        
        dfs(root)
        return self.result

    def invertBinaryTree_a(self, root:TreeNode) -> TreeNode:
        """
        45. 이진 트리 반전
        a. Pythonic(재귀)
        """
        if root:
            root.left, root.right = \
                self.invertBinaryTree_a(root.right), self.invertBinaryTree_a(root.left)
            return root
        return None # 생략 가능, 파이썬은 아무것도 return하지 않으면 None을 return
    
    def invertBinaryTree_b(self, root:TreeNode) -> TreeNode:
        """
        45. 이진 트리 반전
        b. 반복 구조로 BFS
        """
        queue = collections.deque([root])
        while queue:
            node = queue.popleft()
            if node:
                node.left, node.right = node.right, node.left
                
                # 자식 노드가 반복적으로 큐에 삽입됩니다.
                queue.append(node.left)
                queue.append(node.right) 
            
        return root
    
    def invertBinaryTree_c(self, root:TreeNode) -> TreeNode:
        """
        45. 이진 트리 반전
        c. 반복 구조로 DFS
        """
        stack = collections.deque([root])
        while stack:
            node = stack.pop() # pop으로 가장 최근에 추가된 노드부터 탐색
            if node: 
                node.left, node.right = node.right, node.left
                
                # 자식 노드가 반복적으로 큐에 삽입됩니다.
                stack.append(node.left)
                stack.append(node.right) 
            
        return root   

    def invertBinaryTree_d(self, root:TreeNode) -> TreeNode:
        """
        45. 이진 트리 반전(leetcode : 226. Invert Binary Tree)
        d. 반복 구조로 DFS 후위 순회
        """
        stack = collections.deque([root])
        while stack:
            node = stack.pop()
            if node: 
                stack.append(node.left)
                stack.append(node.right) 
                
                node.left, node.right = node.right, node.left
            
        return root   
    
    def mergeTwoBinaryTrees(self, t1:TreeNode, t2:TreeNode) -> TreeNode:
        """
        46. 두 이진 트리 병합(leetcode : 617. Merge Two Binary Trees)
        a. 재귀 탐색
        """
        if t1 and t2:
            node = TreeNode(t1.val + t2.val)
            node.left = self.mergeTwoBinaryTrees(t1.left, t2.left)
            node.right = self.mergeTwoBinaryTrees(t1.right, t2.right)
            
            return node
        
        else:
            return t1 or t2 # 어느 한쪽에 노드가 존재하지 않는다면 존재하는 노드만(t1 or t2) 리턴, 양쪽다 존재하지 않으면 None
        
    def serialize(self, root:TreeNode) -> str:
        '''
        47. 이진 트리 직렬화 & 역직렬화
        직렬화
        '''
        queue = collections.deque([root])
        result = ["#"]
        
        while queue:
            node = queue.popleft()
            if node: 
                queue.append(node.left)
                queue.append(node.right) 

                result.append(str(node.val))
            else:
                result.append("#")
        return "".join(result)

    def deserialize(self, data:str) -> TreeNode:
        '''
        47. 이진 트리 직렬화 & 역직렬화
        역직렬화
        '''
        if data == "##": # 예외처리
            return None
        
        nodes = data.split()
        
        root = TreeNode(int(nodes[1]))
        queue = collections.deque([root])
        
        index = 2
        while queue:
            node = queue.popleft()
            if nodes[index] is not "#":
                node.left = TreeNode(int(nodes[index]))
                queue.append(node.left)
        index += 1
        
        if nodes[index] is not "#":
            node.right = TreeNode(int(nodes[index]))
            queue.append(node.right)
        index += 1
        
    def isBalanced(self, root:TreeNode) -> bool:
        '''
        48. 균형 이진 트리(leetcode : 110. Balanced Binary Tree)
        a. 재귀 구조로 높이 차이 계산
        '''
        def check(root):
            if not root:
                return 0
            
            left = check(root.left)
            right = check(root.right)
            
            # 한번 -1이 되면 더 이상 회복되지 않는다.
            if left == -1 or right == -1 or abs(left-right) > 1:
                return -1 
            
            return max(left,right) + 1
        
        return check(root) != -1
    
    def findMinimum(self, n:int, edges:List[List[int]]) -> List[int]:
        '''
        49. 최소 높이 트리
        a. 단계별 리프 노드 제거
        리프 노드를 하나씩 제거해 나가면서 마지막까지 남아 있는 값을 루트로 하면 최소 높이로 트리 구성 가능
        '''
        graph = collections.defaultdict(list) # 무방향 그래프
        for i, j in edges: # 양방향으로 삽입
            graph[i].append(j)
            graph[j].append(i)
            
        leaves = []
        for i in range(n+1):
            if len(graph[i]) == 1:
                leaves.append(i)
        
        while n>2:
            n -= len(leaves)
            new_leaves = []
            for leaf in leaves:
                neighbor = graph[leaf].pop()
                graph[neighbor].remove(leaf)
                
                if len(graph[neighbor]) == 1:
                    new_leaves.append(neighbor)
            
            leaves = new_leaves
        
        return leaves

    def sortedArrayToBST(self, nums:List[int]) -> TreeNode:
        '''
        50. 정렬된 배열의 이진 탐색 트리 변환(leetcode : 108. Convert Sorted Array to Binary Search Time)
        a. 이진 검색 결과를 트리 구성
        '''
        if not nums:
            return None
        
        mid = len(nums) // 2
        
        node = TreeNode(nums[mid])
        node.left = self.sortedArrayToBST(nums[:mid])
        node.right = self.sortedArrayToBST(nums[mid+1:])
        
        return node
    
    var: int = 0
    def bstToGst(self, root: TreeNode) -> TreeNode:
        """
        51. 이진 탐색 트리(BST)를 더 큰 수 함계 트리(GST)로(leetcode : 1038)
        각 노드를 현재값보다 더 큰 값을 가진 모든 노드의 합으로 만들기
        a. 중위 순회로 노드 값 누적
        """
        if root:
            self.bstToGst(root.right)
            self.val += root.val
            root.val = self.val
            self.bstToGst(root.left)
        
        return root
    
    def rangeSumBst_a(self, root:TreeNode, L:int, R:int) -> int:
        """
        52. 이진 탐색 트리 합의 범위(leetcode : 938)
        a. 재귀 구조 DFS & 가지치기
        """
        def dfs(node: TreeNode):
            if not node:
                return 0
            
            if  node.val < L:
                return dfs(node.right)
            elif node.val > R:
                return dfs(node.left)
            else:
                return node.val + dfs(node.left) + dfs(node.right)
            
    def rangeSumBst_b(self, root:TreeNode, L:int, R:int) -> int:
        """
        52. 이진 탐색 트리 합의 범위(leetcode : 938)
        b. 반복 구조 DFS, (BFS로도 가능하다. pop(0)으로 처리)
        """            
        stack, sum = [root], 0
        while stack:
            node = stack.pop()
            if node:
                if node.val > L:
                    stack.append(node.left)
                if node.val < R:
                    stack.append(node.right)
                if L <= node.val <= R:
                    sum += node.val
        return sum
    
    prev = - sys.maxsize
    result = sys.maxsize
    def minDiffInBST_a(self, root:TreeNode) -> int:
        """
        53. 이진 탐색 트리 노드 간 최소거리(leetcode : 783)
        a. 재귀 구조로 중위 순회
        """            
        if root.left:
            self.minDiffInBST(root.left)
            
        self.result = min(self.result, root.val - self.prev)
        self.prev = root.val
        
        if root.right:
            self.minDiffInBST(root.right)
        
        return self.result

    def minDiffInBST_b(self, root:TreeNode) -> int:
        """
        53. 이진 탐색 트리 노드 간 최소거리(leetcode : 783)
        b. 반복 구조로 중위 순회
        """
        prev = -sys.maxsize
        result = sys.maxsize
        
        stack = []
        node = root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            
            node = stack.pop()
            
            result = min(result, node.val - prev)
            prev = node.val
            
            node = node.right
            
        return result
    
    def buildTree(self, preorder: List[int], inorder: List[int])-> TreeNode:
        """
        54. 전위, 중위 순회 결과로 이진 트리 구축
        a. 전위 순회 결과로 중위 순회 분할 정복
        세 가지 순회중 2가지만 있어도 이진 트리를 복원할 수 있습니다.
        """
        if inorder:
            # 전위 순회의 결과는 중위 순회 분활 인덱스
            index = inorder.index(preorder.pop(0))
            
            # 중위 순회 결과 분할 정복
            node = TreeNode(inorder[index])
            node.left = self.buildTree(preorder, inorder[0 : index])
            node.right = self.buildTree(preorder, inorder[index+1 :])
            
            return node
        
