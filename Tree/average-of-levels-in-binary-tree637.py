''' Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [3.00000,14.50000,11.00000]
Explanation: The average value of nodes on level 0 is 3, on level 1 is 14.5, and on level 2 is 11.
Hence return [3, 14.5, 11].'''

# Simple using BFS and doing sum and divide by len of queue

class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        ans = []

        q = deque([root])

        while q:
            l = len(q)
            s = 0
            for i in range(l):
                node = q.popleft()
                if node:
                    s+=node.val
                if node.left: q.append(node.left)
                if node.right: q.append(node.right)
            
            ans.append(s/l)
        
        return ans
