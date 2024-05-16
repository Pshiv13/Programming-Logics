## Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

## Use BFS technique and add node val of result at right most node at every level.

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        a = []
        q = collections.deque([root])

        while q:
            right = None
            ql = len(q)

            for i in range(ql):
                node = q.popleft()
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            if right:
                a.append(right.val)
                
        return a
