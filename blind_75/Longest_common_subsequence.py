# Problem description here https://leetcode.com/problems/longest-common-subsequence/description/


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        @cache
        def rec(i, j):
            if i >= len(text1) or j >= len(text2):
                return 0

            if text1[i] == text2[j]:
                return 1 + rec(i + 1, j + 1)

            return max(rec(i + 1, j), rec(i, j + 1))

        return rec(0, 0)


# Time Complexity = O(N * M), Space Complexity = O(N * M)
