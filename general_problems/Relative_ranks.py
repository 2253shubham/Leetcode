# Problem description here https://leetcode.com/problems/relative-ranks/description/


class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        rank = [""] * len(score)
        sort_score = np.argsort(score)[::-1]
        rank[sort_score[0]] = "Gold Medal"
        if len(score) == 1:
            return rank
        rank[sort_score[1]] = "Silver Medal"
        if len(score) == 2:
            return rank
        rank[sort_score[2]] = "Bronze Medal"
        if len(score) == 3:
            return rank
        for i in range(3, len(score)):
            rank[sort_score[i]] = str(i + 1)
        return rank


# Time Complexity = O(NlogN), Space Complexity = O(N)
