''' Given the root of a binary tree, return the sum of values of nodes with an even-valued grandparent. If there are no nodes with an even-valued grandparent, return 0.

A grandparent of a node is the parent of its parent if it exists.

Example 1:

Input: root = [6,7,8,2,7,1,3,9,null,1,4,null,null,null,5]
Output: 18
Explanation: The red nodes are the nodes with even-value grandparent while the blue nodes are the even-value grandparents. '''

## Using simple DFS traverse the tree and add sum where grandparent is even valued

class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
        self.total = 0
        def dfs(root):
            if root.val%2==0:
                if root.left:
                    if root.left.left:
                        self.total+=root.left.left.val
                    if root.left.right:
                        self.total+=root.left.right.val
                if root.right:
                    if root.right.left:
                        self.total+=root.right.left.val
                    if root.right.right:
                        self.total+=root.right.right.val
                
            if root.right: dfs(root.right)
            if root.left: dfs(root.left)
            return

        dfs(root)
        
        return self.total
