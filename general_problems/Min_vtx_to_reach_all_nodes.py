# Problem description here https://leetcode.com/problems/minimum-number-of-vertices-to-reach-all-nodes/description/


class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        set1 = set()
        set2 = set()
        for i in edges:
            set1.add(i[0])
            set2.add(i[1])
        common = set1 & set2
        set3 = set1 - common
        return list(set3)


# Time Complexity = O(N), Space Complexity = O(N)
