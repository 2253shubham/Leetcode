# Problem description here https://leetcode.com/problems/longest-consecutive-sequence/description/


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        num_s = set(nums)
        max_lcs = 1

        for i in num_s:
            if i - 1 not in num_s:
                curr = i
                c_lcs = 1

                while curr + 1 in num_s:
                    c_lcs += 1
                    curr += 1

                max_lcs = max(max_lcs, c_lcs)

        return max_lcs


# Time Complexity = O(N), Space Complexity = O(1)
