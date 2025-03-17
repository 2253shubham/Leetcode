# Problem description here https://leetcode.com/problems/excel-sheet-column-title/description/


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        out = ""
        while columnNumber > 0:
            out = chr(ord("A") + (columnNumber - 1) % 26) + out
            columnNumber = (columnNumber - 1) // 26
        return out


# Time Complexity = O(logN), Space Complexity = O(1)
