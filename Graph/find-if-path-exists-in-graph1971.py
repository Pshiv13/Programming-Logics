''' There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.

You want to determine if there is a valid path that exists from vertex source to vertex destination.

Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

Example 1:

Input: n = 3, edges = [[0,1],[1,2],[2,0]], source = 0, destination = 2
Output: true
Explanation: There are two paths from vertex 0 to vertex 2:
- 0 → 1 → 2
- 0 → 2 '''

# Using recursive DFS

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        seen = set()
        graph = defaultdict(list)
        seen.add(source)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        def dfs(i):
            if i == destination: 
                return True
            
            for nei in graph[i]:
                if nei not in seen:
                    seen.add(nei)
                    if dfs(nei):
                        return True
            return False

        return dfs(source)

# Using iterative DFS

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        seen = set()
        graph = defaultdict(list)
        seen.add(source)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        stack = [source]
        while stack:
            node = stack.pop()
            if node == destination: 
                return True
            for i in graph[node]:
                if i not in seen:
                    seen.add(i)
                    stack.append(i)
        
        if len(stack) == 0: return False

# Using BFS

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source == destination: return True
        seen = set()
        graph = defaultdict(list)
        seen.add(source)
        q = deque()
        q.append(source)

        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)
        
        while q:
            l = len(q)

            for j in range(l):
                node = q.popleft()
                if node == destination: 
                    return True
                for i in graph[node]:
                    if i not in seen:
                        seen.add(i)
                        q.append(i)
        
        return False
