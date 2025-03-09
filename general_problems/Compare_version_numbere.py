# Problem description here https://leetcode.com/problems/compare-version-numbers/description/


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        l1 = version1.split(".")
        l2 = version2.split(".")
        l1.append("0")
        l2.append("0")
        maxl = max(len(l1), len(l2))
        cl1 = 0
        cl2 = 0
        f1 = 0
        f2 = 0
        for i in range(maxl):
            if i >= len(l1):
                cl1 = len(l1) - 1
                cl2 = i
            elif i >= len(l2):
                cl2 = len(l2) - 1
                cl1 = i
            else:
                cl1 = i
                cl2 = i
            if int(l1[cl1]) > int(l2[cl2]):
                return 1
            elif int(l1[cl1]) < int(l2[cl2]):
                return -1
            else:
                continue
        return 0


# Time Complexity = O(N), Space Complexity = O(N)
