# Problem description here https://leetcode.com/problems/two-sum/description/


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            if target - num in seen:
                return [seen[target - num], i]
            if num not in seen:
                seen[num] = i


# Time Complexity = O(N), Space Complexity = O(N)
