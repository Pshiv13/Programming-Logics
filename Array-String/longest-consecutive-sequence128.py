""" Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4. """

## check prev number in set or not first to find out starting of the string.
## If prev number is in string then dont apply logic, if it is not in string then start i+1 in loop.


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums)
        longest = 0
        for i in nums:
            if i - 1 not in s:
                current_len = 1
                n = i + 1
                while n in s:
                    current_len += 1
                    n += 1
                longest = max(current_len, longest)
        return longest
