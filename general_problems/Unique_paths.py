# Problem description here https://leetcode.com/problems/unique-paths/description/


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        un_p = [[[0] for j in range(n)] for i in range(m)]
        for i in range(m):
            un_p[i][0] = 1
        for j in range(n):
            un_p[0][j] = 1
        for i in range(1, m):
            for j in range(1, n):
                un_p[i][j] = un_p[i - 1][j] + un_p[i][j - 1]

        return un_p[m - 1][n - 1]


# Time Complexity = O(N * M), Space Complexity = O(N * M)

"""
# Best Solution (O(N * M) time and O(N) space complexity), understand this

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        dp = [1] * n  # Initialize a 1D DP array with all 1s
        
        for i in range(m - 1):  # Iterate from second-last row to top
            for j in range(n - 2, -1, -1):  # Iterate from second-last column to left
                dp[j] += dp[j + 1]  # Update current cell based on right cell
        
        return dp[0]  # The final result is in dp[0]

        
# Alternate Solution (worse Time Complexity (O(2 ^ (m + n))), O(1) Space Complexity)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        self.count = 0
        def dp(i, j):
            if i == m - 1 and j == n - 1:
                self.count = 1
            else:
                if i == m - 1 and j < n - 1:
                    self.count = 1
                elif i < m - 1 and j == n - 1:
                    self.count = 1
                else:
                    self.count = dp(i + 1, j) + dp(i, j + 1)
            return self.count
        return dp(0, 0)
"""
