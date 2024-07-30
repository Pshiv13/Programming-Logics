''' Given the root of a perfect binary tree, reverse the node values at each odd level of the tree.

For example, suppose the node values at level 3 are [2,1,3,4,7,11,29,18], then it should become [18,29,11,7,4,3,1,2].
Return the root of the reversed tree.

A binary tree is perfect if all parent nodes have two children and all leaves are on the same level.

The level of a node is the number of edges along the path between it and the root node. '''

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        q = deque()
        q.append(root)
        L = 0

        while q:
            ln = len(q)

            if L%2 != 0:
                vals = [node.val for node in q]
                for i in range(ln):
                    q[i].val = vals[ln - 1 - i]
                
            for _ in range(ln):
                node = q.popleft()
                if node.left:
                    q.append(node.left)
                    q.append(node.right)
            L += 1
        return root
