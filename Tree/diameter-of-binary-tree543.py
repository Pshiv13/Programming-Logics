""" Given the root of a binary tree, return the length of the diameter of the tree.

The diameter of a binary tree is the length of the longest path between any two nodes in a tree. This path may or may not pass through the root.

The length of a path between two nodes is represented by the number of edges between them. """

## Bottom up
## height = 1+ max(left height, right height)
## Diameter = left height + right height


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        l_d = [0]

        def height(root):
            if not root:
                return 0
            lh = height(root.left)
            rh = height(root.right)
            dm = lh + rh
            l_d[0] = max(l_d[0], dm)
            return 1 + max(lh, rh)

        height(root)
        return l_d[0]
