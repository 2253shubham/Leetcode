# Problem_description here https://leetcode.com/problems/pacific-atlantic-water-flow/description/

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        if not heights:
            return []
        l = len(heights)
        b = len(heights[0])
        p_v = set()
        a_v = set()

        def dfs(i, j, visited):
            visited.add((i, j))
            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):
                if (
                    0 <= x < l
                    and 0 <= y < b
                    and heights[x][y] >= heights[i][j]
                    and (x, y) not in visited
                ):
                    dfs(x, y, visited)

        for i in range(l):
            dfs(i, 0, p_v)
            dfs(i, b - 1, a_v)

        for j in range(b):
            dfs(0, j, p_v)
            dfs(l - 1, j, a_v)

        return list(p_v & a_v)


# Time Complexity = O(M * N), Space Complexity = O(M * N)