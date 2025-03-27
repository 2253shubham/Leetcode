# Problem description here https://leetcode.com/problems/minimum-number-of-moves-to-seat-everyone/description/


class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        mse = sorted(seats)
        msu = sorted(students)
        diff = 0
        for i in range(len(seats)):
            diff += abs(mse[i] - msu[i])
        return diff


# Time Complexity = O(NlogN), Space Complexity = O(N)
