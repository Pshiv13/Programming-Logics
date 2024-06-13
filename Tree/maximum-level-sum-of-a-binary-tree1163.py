''' Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

Example 1:

Input: root = [1,7,0,7,-8,null,null]
Output: 2
Explanation: 
Level 1 sum = 1.
Level 2 sum = 7 + 0 = 7.
Level 3 sum = 7 + -8 = -1.
So we return the level with the maximum sum which is level 2. '''

# Using normal BFS to iterate and calculate sum of each level

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        maxLevel = [0]
        maxTotal = [float('-inf')]
        q = deque([root])

        if root.left is None and root.right is None: return 1

        def bfs(lev):
            while q:
                qLen = len(q)
                curTotal = 0
                for _ in range(qLen):
                    n = q.popleft()
                    curTotal += n.val
                    if n.left is not None: q.append(n.left)
                    if n.right is not None: q.append(n.right)
                lev += 1
                if curTotal > maxTotal[0]:
                    maxTotal[0] = curTotal
                    maxLevel[0] = lev

        bfs(0)
        return maxLevel[0]
