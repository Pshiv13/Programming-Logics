""" You are given a 0-indexed 2D integer matrix grid of size n * n with values in the range [1, n2]. Each integer appears exactly once except a which appears twice and b which is missing. The task is to find the repeating and missing numbers a and b.
Return a 0-indexed integer array ans of size 2 where ans[0] equals to a and ans[1] equals to b.
Example 1:
Input: grid = [[1,3],[2,2]]
Output: [2,4]
Explanation: Number 2 is repeated and number 4 is missing so the answer is [2,4]."""


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        ans = [0] * 2
        mapp = {}

        l = len(grid)
        maxx = l * l
        minn = 1

        for i in grid:
            for j in i:
                if j in mapp:
                    mapp[j] = 2
                else:
                    mapp[j] = 1

        for i in range(1, maxx + 1):
            if i not in mapp:
                ans[1] = i
                continue

            if mapp[i] == 2:
                ans[0] = i

        return ans
