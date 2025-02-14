# Problem description here https://leetcode.com/problems/longest-repeating-character-replacement/description/


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0
        maxl = 0
        charc = [0] * 26

        while right < len(s):
            charc[ord(s[right]) - ord("A")] += 1

            while sum(charc) - max(charc) > k and left < right:
                charc[ord(s[left]) - ord("A")] -= 1
                left += 1

            maxl = max(maxl, right - left + 1)
            right += 1

        return maxl


# Time Complexity = O(N), Space Complexity = O(N)
