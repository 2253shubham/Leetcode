# Problem description here https://leetcode.com/problems/house-robber/


class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        prev_m = 0
        curr_m = 0
        for i in range(len(nums)):
            temp = max(curr_m, prev_m + nums[i])
            prev_m = curr_m
            curr_m = temp

        return curr_m


# Time Complexity = O(N), Space Complexity = O(1)

"""

# Alternate way

class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        dp = [0] * len(nums)
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        maxm = 1
        for i in range(2, len(nums)):
            c = maxm - 1
            if (nums[i] + dp[c]) > dp[maxm]:
                dp[i] = nums[i] + dp[c]
            else:
                dp[i] = dp[maxm]
            maxm = i
        
        return dp[-1]

# Time Complexity = O(N), Space Complexity = O(N)

"""
