# Problem description here https://leetcode.com/problems/counting-bits/description/


class Solution:
    def countBits(self, n: int) -> List[int]:
        dp = [0] * (n + 1)
        offset = 1

        for i in range(1, n + 1):
            if offset * 2 == i:
                offset = i

            dp[i] = 1 + dp[i - offset]

        return dp


# Time Complexity = O(N), Space Complexity = O(N)

"""
# My original code

    def countBits(self, n: int) -> List[int]:
        out = []
        for i in range(n+1):
            binary = bin(i)
            out.append(Counter(binary)['1'])
        
        return out
"""
