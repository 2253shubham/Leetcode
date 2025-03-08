# Problem description here https://leetcode.com/problems/minimize-the-difference-between-target-and-chosen-elements/description/


class Solution:
    def minimizeTheDifference(self, mat: List[List[int]], target: int) -> int:
        self.cur_min = float(inf)

        @cache
        def dp(row, summ):
            if row == len(mat):
                self.cur_min = min(self.cur_min, abs(target - summ))
                return abs(target - summ)
            if summ - target > self.cur_min:
                return float(inf)
            minm = float(inf)
            for i in set(mat[row]):
                diff = dp(row + 1, summ + i)
                minm = min(minm, diff)
                if minm == 0:
                    return 0
            return minm

        return dp(0, 0)


# Time Complexity = O(2^N * M), Space Complexity = O(N * T)
# Where M is the number of rows and N is the number of columns
# Understand time and space complexity!!
