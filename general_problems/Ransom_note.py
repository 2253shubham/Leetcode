# Problem description here https://leetcode.com/problems/ransom-note/description/


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        lr = len(ransomNote)
        lm = len(magazine)
        if lm < lr:
            return False
        dp = [0] * 26
        for i in range(lm):
            dp[ord(magazine[i]) - ord("a")] += 1
            if i < lr:
                dp[ord(ransomNote[i]) - ord("a")] -= 1

        for i in range(26):
            if dp[i] < 0:
                return False

        return True


# Time Complexity = O(N), Space Complexity O(1)
# Space Complexity is precisely O(26) which is still O(1)
