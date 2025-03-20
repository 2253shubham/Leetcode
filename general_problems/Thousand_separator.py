# Problem description here https://leetcode.com/problems/thousand-separator/description/


class Solution:
    def thousandSeparator(self, n: int) -> str:
        l = len(str(n))
        word = ""
        count = 0
        for i in range(l):
            if count == 3:
                word += "."
                count = 0
            count += 1
            word += str(n)[::-1][i]
        return word[::-1]


# Time Complexity = O(N), Space Complexity = O(N)
# where N is the length of str(n)
