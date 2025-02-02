# Problem description here https://leetcode.com/problems/palindromic-substrings/description/


class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def check(i, j, count):
            while i > -1 and j < len(s) and s[i : j + 1] == s[i : j + 1][::-1]:
                count += 1
                i -= 1
                j += 1
            return count

        for i in range(len(s)):
            count = check(i, i, count)
            count = check(i, i + 1, count)

        return count


# Time Complexity = O(N^2), Space Complexity = O(1)
