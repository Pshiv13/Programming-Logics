''' Given the root of a binary tree, return its maximum depth.

A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node. '''


## Using iterative approach

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        return max(1+self.maxDepth(root.left), 1+self.maxDepth(root.right))

## Using BFS approach

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        level = 0
        q = deque([root])
        while q:
            for i in range(len(q)):
                t = q.popleft()
                if t.left: q.append(t.left)
                if t.right: q.append(t.right)
            level+=1
        return level

## Using DFS approach

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        res = 1
        stack = [[root, 1]]
        while stack:
            node, depth = stack.pop()
            if node:
                stack.append([node.left, depth+1])
                stack.append([node.right, depth+1])
                res = max(res, depth)
        return res
