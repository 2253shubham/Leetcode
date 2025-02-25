# Problem description here https://leetcode.com/problems/rotate-function/description/

import numpy as np


class Solution:
    def maxRotateFunction(self, nums: List[int]) -> int:
        tot_sum = sum(nums)
        cur_sum = sum([i * nums[i] for i in range(len(nums))])
        max_sum = cur_sum

        for i in range(1, len(nums)):
            cur_sum = (
                cur_sum
                - nums[len(nums) - i] * (len(nums) - 1)
                + tot_sum
                - nums[len(nums) - i]
            )

            max_sum = max(max_sum, cur_sum)

        return max_sum


# Time Complexity = O(N), Space Complexity = O(1)
