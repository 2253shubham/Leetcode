# Problem description here https://leetcode.com/problems/combination-sum-iv/description/


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        memo = {}

        def dfs(target):
            if target == 0:
                return 1  # Found a valid combination
            if target in memo:
                return memo[target]  # Use precomputed result

            count = 0
            for num in nums:
                if target - num >= 0:
                    count += dfs(target - num)

            memo[target] = count  # Store computed result
            return count

        return dfs(target)


# Time Complexity = O(N * T), Space Complexity = O(T)
# Where T is the number of combinations

"""

# Alternate solution (Bottoms-up approach, same time and space complexity)

class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1  # Base case: one way to make sum 0 (empty set)

        for t in range(1, target + 1):
            for num in nums:
                if t - num >= 0:
                    dp[t] += dp[t - num]

        return dp[target]

"""
