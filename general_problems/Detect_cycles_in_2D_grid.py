# Problem description here https://leetcode.com/problems/detect-cycles-in-2d-grid/description/


class Solution:
    def containsCycle(self, grid: List[List[str]]) -> bool:
        row, col = len(grid), len(grid[0])
        visited = set()

        def neighbors(r, c):
            return [
                (i, j)
                for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                if 0 <= i < row and 0 <= j < col and grid[i][j] == grid[r][c]
            ]

        def dfs(r, c, prev, seen):
            if (r, c) in seen:
                return True
            seen.add((r, c))
            visited.add((r, c))

            for i, j in neighbors(r, c):
                if not prev or prev != (i, j):
                    if dfs(i, j, (r, c), seen):
                        return True
            return False

        for i in range(row):
            for j in range(col):
                if (i, j) not in visited:
                    seen = set()
                    if dfs(i, j, None, seen):
                        return True

        return False


# Time Complexity = O(M * N), Space Complexity = O(M * N)
# where M is the number of rows and N is the number of columns
