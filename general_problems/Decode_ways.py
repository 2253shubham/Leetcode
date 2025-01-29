# Problem description here https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:
        
        def dp(s, memo):
            if s in memo:
                return memo[s]
            if not s or (len(s) == 1 and s[0] != "0"):
                return 1
            if s[0] == "0":
                return 0

            removeOne = dp(s[1:], memo)
            removeTwo = 0 if int(s[:2]) > 26 else dp(s[2:], memo)

            memo[s] = removeOne + removeTwo
            return memo[s]

        return dp(s, {})
    
# Time Complexity = O(N), Space Complexity = O(N)
