class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:

        def sameTree(p, q):
            if not p and not q:
                return True
            if (p and not q) or (q and not p):
                return False
            if p.val != q.val:
                return False
            return sameTree(p.left, q.left) and sameTree(p.right, q.right)

        def hasSubTree(root):
            if not root:
                return False
            if sameTree(root, subRoot):
                return True
            return hasSubTree(root.left) or hasSubTree(root.right)

        return hasSubTree(root)
