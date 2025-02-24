# Problem description here https://leetcode.com/problems/is-subsequence/description/


class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            return False
        cs = 0
        ct = 0
        while cs < len(s) and ct < len(t):
            if s[cs] == t[ct]:
                cs += 1
                ct += 1
            else:
                ct += 1
        if cs == len(s):
            return True
        else:
            return False


# Time Complexity = O(T), Space Complexity = O(1)
# where T is the length of the larger string
