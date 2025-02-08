# Problem description here https://leetcode.com/problems/maximum-subarray/description/


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxm = nums[0]
        cmax = nums[0]
        for i in nums[1:]:
            maxm = max(i, i + maxm)
            cmax = max(cmax, maxm)

        return cmax


# Time Complexity = O(N), Space Complexity = O(1)
