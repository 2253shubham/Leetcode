# Problem description here https://leetcode.com/problems/sqrtx/description/


class Solution:
    def mySqrt(self, x: int) -> int:
        lo = 0
        hi = x + 1
        mid = x // 2

        while hi - lo > 1:
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                lo = mid
            else:
                hi = mid
            mid = lo + (hi - lo) // 2

        return mid


# Time Complexity = O(logN), Space Complexity = O(1)
