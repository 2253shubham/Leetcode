# Problem description here https://leetcode.com/problems/house-robber-ii/description/


class Solution:
    def rob(self, nums: List[int]) -> int:
        def dp(nums):
            prev_m = 0
            curr_m = 0
            for i in range(len(nums)):
                temp = max(curr_m, prev_m + nums[i])
                prev_m = curr_m
                curr_m = temp
            return curr_m

        return max(nums[0], dp(nums[1:]), dp(nums[:-1]))


# Time Complexity = O(N), Space Complexity = O(1)
