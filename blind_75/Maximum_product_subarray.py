# Problem description here https://leetcode.com/problems/maximum-product-subarray/description/


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxm, minm = 1, 1
        res = nums[0]

        for i in range(len(nums)):
            curr = [nums[i], nums[i] * maxm, nums[i] * minm]
            maxm = max(curr)
            minm = min(curr)
            res = max(res, maxm)

        return res


# Time Complexity = O(N), Space Complexity = O(1)
