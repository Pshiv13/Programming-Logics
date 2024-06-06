""" Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

The left 
subtree
 of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees. 

Example 1:

Input: root = [2,1,3]
Output: true """


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        a = []

        def trav(root):
            if root.left is not None:
                trav(root.left)
            a.append(root.val)
            if root.right is not None:
                trav(root.right)

        trav(root)

        if len(a) != len(set(a)):
            return False
        return sorted(a) == a
