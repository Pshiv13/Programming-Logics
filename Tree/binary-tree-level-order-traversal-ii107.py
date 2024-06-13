''' Given the root of a binary tree, return the bottom-up level order traversal of its nodes' values. (i.e., from left to right, level by level from leaf to root).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[15,7],[9,20],[3]]
Example 2:

Input: root = [1]
Output: [[1]]
Example 3:

Input: root = []
Output: [] '''

# Using simple BFS

class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        res = []
        q = deque([root])

        while q:
            qLen = len(q)
            a = []
            for _ in range(qLen):
                n = q.popleft()
                if n:
                    a.append(n.val)
                    if n.left: q.append(n.left)
                    if n.right: q.append(n.right)
            if len(a)>0:
                res.append(a)
        
        return(res[::-1])
