''' Example 1
Input: nums = [3,2,1,5,6,4], k = 2
Output: 5 '''

## Remove top two element and append their diff to heap.
## heapq by default min heap so convert all element to (-1)* element

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        for i in range(len(stones)):
            stones[i] = (-1) * stones[i]

        heapq.heapify(stones)

        while len(stones) > 1:
            largest = heapq.heappop(stones)
            second = heapq.heappop(stones)

            if largest != second:
                heapq.heappush(stones, largest - second)

        if len(stones) == 1:
            return (-1) * (heapq.heappop(stones))
        else:
            return 0
