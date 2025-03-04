# Problem description here https://leetcode.com/problems/partition-equal-subset-sum/description/


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        sumn = sum(nums)
        if sumn % 2 != 0:
            return False  # Cannot partition if the total sum is odd

        target = sumn // 2
        dp = [False] * (target + 1)
        dp[0] = True  # Base case: A subset sum of 0 is always possible

        for num in nums:
            for j in range(target, num - 1, -1):  # Iterate backwards
                dp[j] = dp[j] or dp[j - num]

        return dp[target]


# Time Complexity = O(N), Space Complexity = O(1)
