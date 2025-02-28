# Problem description here https://leetcode.com/problems/nth-digit/description/


class Solution:
    def findNthDigit(self, n: int) -> int:
        i = 1
        while (i * 9 * 10 ** (i - 1)) < n:
            n -= i * 9 * 10 ** (i - 1)
            i += 1
        div = n // i
        mod = n % i

        if mod == 0:
            return int(str(10 ** (i - 1) + div - 1)[-1])
        else:
            return int(str(10 ** (i - 1) + div)[mod - 1])


# Time Complexity = O(logN), Space Complexity = O(1)


"""

# Alternate solution using Binary search (Same time and space complexity)

class Solution:
    def findNthDigit(self, n: int) -> int:
        digit_in_num = 1
        start = 1
        end = 9

        while n > digit_in_num * end:
            n -= digit_in_num * end
            digit_in_num += 1
            start *= 10
            end *= 10

        num = start + (n - 1) // digit_in_num
        return int(str(num)[(n - 1) % digit_in_num])

"""
