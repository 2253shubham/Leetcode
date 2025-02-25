# Problem description here https://leetcode.com/problems/integer-replacement/


class Solution:
    def integerReplacement(self, n: int) -> int:
        counter = 0
        while n != 1:
            if n % 2 == 0:
                n = n // 2
            else:
                if n & 3 == 3 and n != 3:
                    n += 1
                else:
                    n -= 1
            counter += 1

        return counter


# Time Complexity = O(logN), Space Complexity = O(1)
