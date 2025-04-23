# Problem description here https://leetcode.com/problems/rank-transform-of-an-array/description/

class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        sorta = sorted(set(arr))
        rd = {}
        for ind, val in enumerate(sorta):
            rd[val] = ind + 1
        res = []
        for num in arr:
            res.append(rd[num])

        return res
    
# Time Complexity = O(NlogN), Space Complexity = O(N)