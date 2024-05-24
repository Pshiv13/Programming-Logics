### Given the root of a binary tree, invert the tree, and return its root.

## Using recursion. Swap the left and right nodes at every root and do DFS using recursion.


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return None
        temp = root.left
        root.left = root.right
        root.right = temp
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
