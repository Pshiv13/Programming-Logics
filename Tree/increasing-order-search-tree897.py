""" Given the root of a binary search tree, rearrange the tree in in-order so that the leftmost node in the tree is now the root of the tree, 
and every node has no left child and only one right child.

Example 1:

Input: root = [5,3,6,2,4,null,8,1,null,null,null,7,9]
Output: [1,null,2,null,3,null,4,null,5,null,6,null,7,null,8,null,9] """


class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        INORD = []

        def dfs(root):
            if root.left is not None:
                dfs(root.left)
            INORD.append(root.val)
            if root.right is not None:
                dfs(root.right)

        dfs(root)

        D = TreeNode()
        root = TreeNode(INORD[0])
        D.right = root

        for i in range(1, len(INORD)):
            root.right = TreeNode(INORD[i])
            root = root.right

        return D.right
