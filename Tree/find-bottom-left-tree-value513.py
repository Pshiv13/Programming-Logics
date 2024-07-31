''' Given the root of a binary tree, return the leftmost value in the last row of the tree. '''

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        LEFTMOST = 0

        q = deque()
        q.append(root)

        while(q):
            L = len(q)
            LEFTMOST = q[0].val
            for _ in range(L):
                N = q.popleft()
                if N.left: q.append(N.left)
                if N.right: q.append(N.right)
        
        return LEFTMOST
