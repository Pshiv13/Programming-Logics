''' Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1 '''

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        a = []

        def d(root):
            if root.left is not None: d(root.left)
            a.append(root.val)
            if root.right is not None: d(root.right)

        d(root)

        return a[k-1]
