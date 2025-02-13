# Problem description here https://leetcode.com/problems/sum-of-two-integers/description/


class Solution:
    def getSum(self, a: int, b: int) -> int:
        MASK = 0xFFFFFFFF  # 32-bit mask
        MAX_INT = 0x7FFFFFFF  # Max positive integer for 32-bit

        def add(a, b):
            while b != 0:
                carry = (a & b) & MASK
                a = (a ^ b) & MASK
                b = (carry << 1) & MASK
            # If a is a negative number in 32-bit, convert it to Python’s negative integer
            return a if a <= MAX_INT else ~(a ^ MASK)

        return add(a, b)


# Time Complexity O(1), Space Complexity = O(1)
# (Worst case, bit gets shifted by 32 times, O(32))
