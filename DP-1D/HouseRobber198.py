## You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.
## Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

##  [rob1, rob2, n , n+1, ...]


class Solution:
    def rob(self, nums: List[int]) -> int:
        # [rob1, rob2, n , n+1, ...]
        rob1, rob2 = 0, 0
        for n in nums:
            temp = max(n + rob1, rob2)
            rob1 = rob2
            rob2 = temp
        return rob2
