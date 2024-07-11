''' Given the root of a binary tree, flatten the tree into a "linked list":
The "linked list" should use the same TreeNode class where the right child pointer points to the next node in the list and the left child pointer is always null.
The "linked list" should be in the same order as a pre-order traversal of the binary tree.

Example 1:
Input: root = [1,2,5,3,4,null,6]
Output: [1,null,2,null,3,null,4,null,5,null,6]

Example 2:
Input: root = []
Output: []
Example 3:

Input: root = [0]
Output: [0]'''

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if not root: return root

        PRE = []

        def dfs(root):
            PRE.append(root)
            if root.left is not None:
                dfs(root.left)
            if root.right is not None:
                dfs(root.right)
        
        dfs(root)
        
        L = len(PRE)

        for i in range(L-1):
            PRE[i].left = None
            PRE[i].right = PRE[i+1]
        
        return PRE[0]
