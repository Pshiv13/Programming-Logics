''' Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:

Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped. '''


## find max of in all left element list
## Find max of all right element list
## water += min(max_left, max_right) - height[i]


class Solution:
    def trap(self, height: List[int]) -> int:
        lw = 0
        rw = 0
        l = len(height)

        max_l = [0]*l
        max_r = [0]*l

        for i in range(l):
            j = -i-1
            max_l[i] = lw
            max_r[j] = rw

            lw = max(lw, height[i])
            rw = max(rw, height[j])
        
        summ = 0
        for i in range(l):
            summ += max(0, (min(max_l[i], max_r[i])) - height[i])
        return summ
