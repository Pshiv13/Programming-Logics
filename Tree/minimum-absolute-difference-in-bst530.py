""" Given the root of a Binary Search Tree (BST), return the minimum absolute difference between the values of any two different nodes in the tree.
Example 1:
Input: root = [4,2,6,1,3]
Output: 1

Example 2:
Input: root = [1,0,48,null,null,12,49]
Output: 1"""


class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        val = []

        def dfs(root):
            if root.left is not None:
                dfs(root.left)
            val.append(root.val)
            if root.right is not None:
                dfs(root.right)

        dfs(root)
        smallD = float(inf)

        for i in range(len(val) - 1):
            smallD = min(smallD, -(val[i] - val[i + 1]))

        return smallD
