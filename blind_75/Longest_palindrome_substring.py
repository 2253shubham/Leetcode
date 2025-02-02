# Problem description here https://leetcode.com/problems/longest-palindromic-substring/submissions/1528039847/


class Solution:
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s

        def check(i, j):
            while i > -1 and j < len(s) and s[i] == s[j]:
                i -= 1
                j += 1
            return s[i + 1 : j]

        maxs = s[0]
        for i in range(len(s) - 1):
            w1 = check(i, i)
            w2 = check(i, i + 1)

            if len(w1) > len(w2):
                if len(maxs) < len(w1):
                    maxs = w1
            else:
                if len(maxs) < len(w2):
                    maxs = w2

        return maxs


# Time Complexity = O(N^2), Space Complexity = O(1)
