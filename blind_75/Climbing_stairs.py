# Problem description here https://leetcode.com/problems/climbing-stairs/


class Solution:
    def climbStairs(self, n: int) -> int:
        prev_i = 2
        prev_ii = 1
        curr = prev_i if n == 2 else prev_ii
        for i in range(3, n + 1):
            curr = prev_i + prev_ii
            prev_ii = prev_i
            prev_i = curr

        return curr


# Time Complexity = O(N), Space Complexity = O(1)
