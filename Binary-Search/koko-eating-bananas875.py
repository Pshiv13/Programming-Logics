''' Koko loves to eat bananas. There are n piles of bananas, the ith pile has piles[i] bananas. The guards have gone and will come back in h hours.

Koko can decide her bananas-per-hour eating speed of k. Each hour, she chooses some pile of bananas and eats k bananas from that pile. If the pile has less than k bananas, she eats all of them instead and will not eat any more bananas during this hour.

Koko likes to eat slowly but still wants to finish eating all the bananas before the guards return.

Return the minimum integer k such that she can eat all the bananas within h hours.

Example 1:

Input: piles = [3,6,7,11], h = 8
Output: 4 '''

## Max banan per hour can koko eat is max(piles)
## We can use 1 to max(piles) using binary search

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def k_found(k):
            hour = 0
            for i in piles:
                hour+=ceil(i/k)
            return hour <= h
        
        l = 1
        r = max(piles)

        while(l<r):
            m = (l+r)//2
            if k_found(m):
                r = m
            else:
                l = m+1
        
        return r
