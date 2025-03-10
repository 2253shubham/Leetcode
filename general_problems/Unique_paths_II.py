# Problem description here https://leetcode.com/problems/unique-paths-ii/description/


class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0
        un_p = [[0 for j in range(n)] for i in range(m)]
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                break
            un_p[0][j] = 1
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                break
            un_p[i][0] = 1
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    continue
                un_p[i][j] = un_p[i - 1][j] + un_p[i][j - 1]

        return un_p[m - 1][n - 1]


# Time Complexity = O(N * M), Space Complexity = O(N * M)

"""
# Best Solution (O(N * M) time and O(N) space complexity), understand this

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m, n = len(obstacleGrid), len(obstacleGrid[0])
        
        # If start or end is blocked, return 0
        if obstacleGrid[0][0] == 1 or obstacleGrid[m - 1][n - 1] == 1:
            return 0

        dp = [0] * n
        dp[0] = 1  # Start position
        
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[j] = 0  # Blocked cell → No paths
                elif j > 0:
                    dp[j] += dp[j - 1]  # Sum paths from left

        return dp[-1]

"""