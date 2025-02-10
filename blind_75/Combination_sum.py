# Problem description here https://leetcode.com/problems/combination-sum/


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(idx, candidates, target, ar, res):
            if target == 0:
                res.append(ar[:])
                return
            else:
                for i in range(idx, len(candidates)):
                    if target - candidates[i] >= 0:
                        ar.append(candidates[i])
                        dfs(i, candidates, target - candidates[i], ar, res)
                        ar.pop()

        dfs(0, candidates, target, [], res)

        return res


# Time Complexity = O(N ^ M/2), Space Complexity = O(N ^ M/2)
# Where M is the target value and N is the size of candidates list
