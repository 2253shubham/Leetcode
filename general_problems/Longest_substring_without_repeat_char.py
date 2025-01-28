# Problem description here https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        ch = set()
        gmax = 0

        for right in range(len(s)):
            while s[right] in ch:
                ch.remove(s[left])
                left += 1
            ch.add(s[right])
            gmax = max(gmax, right - left + 1)
        return gmax

# Time Complexity = O(N), Space Complexity = O(N)