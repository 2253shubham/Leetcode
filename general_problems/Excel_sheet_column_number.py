# Problem description here https://leetcode.com/problems/excel-sheet-column-number/description/


class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        k = len(columnTitle)
        num = 0
        for l in range(k):
            num += (ord(columnTitle[l]) - ord("A") + 1) * (26 ** (k - l - 1))

        return num


# Time Complexity = O(N), Space Complexity = O(1)
