# Problem description here https://leetcode.com/problems/height-checker/description/


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        exh = sorted(heights)

        diff = 0
        for i in range(len(heights)):
            if heights[i] != exh[i]:
                diff += 1

        return diff


# Time Complexity = O(NlogN), Space Complexity = O(N)
