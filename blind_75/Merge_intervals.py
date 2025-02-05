# Problem description here https://leetcode.com/problems/merge-intervals/


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        out = []
        left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if left <= intervals[i][0] <= right:
                if right <= intervals[i][1]:
                    right = intervals[i][1]
            else:
                out.append([left, right])
                left = intervals[i][0]
                right = intervals[i][1]

        out.append([left, right])
        return out


# Time Complexity = O(NlogN), Space Complexity = O(N)
