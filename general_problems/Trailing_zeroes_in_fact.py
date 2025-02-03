# Problem description here https://leetcode.com/problems/factorial-trailing-zeroes/


class Solution:
    def trailingZeroes(self, n: int) -> int:
        tot = 0
        i = 5
        while n / i >= 1:
            tot += int(n / i)
            i *= 5
        return tot


# Time Complexity = O(logN), Space Complexity = O(1)
