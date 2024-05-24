"""
Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
"""

## Two solutions


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}

        for i in nums:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1

        return sorted(d, key=d.get, reverse=True)[:k]


## Second


def moveZeroes(nums, k):
    d = {}
    a = [[] for i in range(len(nums) + 1)]
    res = []
    for i in nums:
        d[i] = 1 + d.get(i, 0)

    for n, c in d.items():
        a[c].append(n)

    for i in range(len(a) - 1, 0, -1):
        for n in a[i]:
            res.append(n)
            if len(res) == k:
                return res
