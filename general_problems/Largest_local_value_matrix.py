# Problem description here https://leetcode.com/problems/largest-local-values-in-a-matrix/description/


class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        output = [[0] * (n - 2) for _ in range(n - 2)]
        for i in range(n - 2):
            for j in range(n - 2):
                output[i][j] = max(max(row[j : j + 3]) for row in grid[i : i + 3])
        return output


# Time Complexity = O(N^2), Space Complexity = O(1)
