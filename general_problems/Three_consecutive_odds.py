# Problem description here https://leetcode.com/problems/three-consecutive-odds/description/


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr) - 2):
            if arr[i] % 2 == 0 or arr[i + 1] % 2 == 0 or arr[i + 2] % 2 == 0:
                i += 3
            else:
                return True
        return False


# Time Complexity = O(N), Space Complexity = O(1)
