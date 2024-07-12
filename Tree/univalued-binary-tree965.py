''' A binary tree is uni-valued if every node in the tree has the same value.
Given the root of a binary tree, return true if the given tree is uni-valued, or false otherwise.
Example 1:
Input: root = [1,1,1,1,1,null,1]
Output: true '''

class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        VAL = set()

        def dfs(root):
            VAL.add(root.val)
            if root.left is not None:
                dfs(root.left)
            if root.right is not None:
                dfs(root.right)
        
        dfs(root)

        return len(VAL) == 1
