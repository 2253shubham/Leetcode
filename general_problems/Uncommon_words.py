# Problem description here https://leetcode.com/problems/uncommon-words-from-two-sentences/description/


class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        k = defaultdict(int)

        for i in s1.split(" "):
            k[i] += 1

        for i in s2.split(" "):
            k[i] += 1

        return [i for i in k if k[i] == 1]


# Time Complexity = O(N), Space Complexity = O(N)
