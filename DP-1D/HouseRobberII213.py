## You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed. All houses at this place are arranged in a circle. That means the first house is the neighbor of the last one. Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

## Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

## Just circular from House robber, and cant select first and last node at same time


class Solution:
    def rob(self, nums: List[int]) -> int:
        # [rob1, rob2, n, n+1, ....]

        return max(nums[0], self.helper(nums[1:]), self.helper(nums[:-1]))

    def helper(self, nums):
        rob1, rob2 = 0, 0

        for n in nums:
            temp = max(rob2, rob1 + n)
            rob1 = rob2
            rob2 = temp

        return rob2
