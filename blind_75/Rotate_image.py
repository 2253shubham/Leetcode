# Problem description here https://leetcode.com/problems/rotate-image/description/


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        low = 0
        high = len(matrix) - 1
        while low < high:
            matrix[low], matrix[high] = matrix[high], matrix[low]
            low += 1
            high -= 1

        for i in range(len(matrix)):
            for j in range(i):
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]


# Time Complexity = O(N^2), Space Complexity = O(1)
