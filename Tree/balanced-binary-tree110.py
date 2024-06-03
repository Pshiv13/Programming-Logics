''' Given a binary tree, determine if it is 
height-balanced.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: true '''

## Using DFS approach and maintain one global variable balanced = True.

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        balanced = [True]

        def height(root):
            if not root: return 0

            left_height = height(root.left)
            
            right_height = height(root.right)

            if abs(left_height - right_height) > 1: 
                balanced[0] = False
                return 0

            return 1 + max(left_height, right_height)
        
        height(root)

        return balanced[0]
