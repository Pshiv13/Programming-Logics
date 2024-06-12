''' Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).

Example 1:

Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
Explanation: Leaf nodes in green with value (target = 2) are removed (Picture in left). 
After removing, new nodes become leaf nodes with value (target = 2) (Picture in center). '''

# Using DFS to iterate over tree c number of times. Where c is number of times target value is present in tree.

class Solution:
    def removeLeafNodes(self, root: Optional[TreeNode], target: int) -> Optional[TreeNode]:
        cur = root
        if not root: return root

        def dfs(i):
            if i.left is not None:
                if i.left.val == target and i.left.left is None and i.left.right is None:
                    i.left = None
            if i.right is not None:
                if i.right.val == target and i.right.left is None and i.right.right is None:
                    i.right = None
            if i.left is not None: dfs(i.left)
            if i.right is not None: dfs(i.right)

        c = [0]
        def d(i):
            if i.val == target: c[0]+=1
            if i.left is not None: d(i.left)
            if i.right is not None: d(i.right)

        d(root)

        for i in range(c[0]):
            dfs(cur)

        if root.left is None and root.right is None and root.val == target: return None
        return root
