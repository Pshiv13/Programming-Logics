''' Given an integer array nums where the elements are sorted in ascending order, convert it to a 
height-balanced binary search tree.

Example 1:

Input: nums = [-10,-3,0,5,9]
Output: [0,-3,9,-10,null,5]
Explanation: [0,-10,5,null,-3,null,9] is also accepted: '''

# Traverse from mid . Go to left and recurssion again and go to right and recurssion again. 

class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def trav(l, r):
            if l>r:
                return None

            m = (l+r) // 2
            root = TreeNode(nums[m])
            root.left = trav(l, m-1)
            root.right = trav(m+1, r)
            return root
        
        return trav(0, len(nums) - 1)
