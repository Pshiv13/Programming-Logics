''' Given the root of a binary tree, return the postorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [3,2,1]
Example 2:

Input: root = []
Output: []
Example 3:

Input: root = [1]
Output: [1] '''

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        
        if not root: return []
        
        def dfs(i):
            if i.left is not None: dfs(i.left)
            if i.right is not None: dfs(i.right)
            res.append(i.val)
        
        dfs(root)
        return res
