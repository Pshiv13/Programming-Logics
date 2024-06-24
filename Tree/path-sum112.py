""" Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.

A leaf is a node with no children.
Example 1:
Input: root = [5,4,8,11,null,13,4,7,2,null,null,null,1], targetSum = 22
Output: true
Explanation: The root-to-leaf path with the target sum is shown."""


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        def dfs(root, curSum):
            if not root:
                return False

            curSum += root.val

            if not root.left and not root.right:
                return curSum == targetSum

            return dfs(root.left, curSum) or dfs(root.right, curSum)

        return dfs(root, 0)
