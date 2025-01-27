# Problem description here https://leetcode.com/problems/last-stone-weight/

import heapq


class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if len(stones) == 1:
            return stones[0]
        stones = [-i for i in stones]
        heapq.heapify(stones)
        while len(stones) != 1:
            m1 = -heapq.heappop(stones)
            m2 = -heapq.heappop(stones)
            diff = m1 - m2
            heapq.heappush(stones, -diff)

        return -stones[0]

# Time Complexity = O(NlogN), Space Complexity = O(NlogN)