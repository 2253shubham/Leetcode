# Problem description here https://leetcode.com/problems/dungeon-game/description/


class Solution:
    def calculateMinimumHP(self, dungeon: List[List[int]]) -> int:
        m = len(dungeon)
        n = len(dungeon[0])

        min_health = [[0] * n for i in range(m)]
        min_health[-1][-1] = max(1, 1 - dungeon[-1][-1])

        for i in range(m - 2, -1, -1):
            min_health[i][-1] = max(1, min_health[i + 1][-1] - dungeon[i][-1])

        for j in range(n - 2, -1, -1):
            min_health[-1][j] = max(1, min_health[-1][j + 1] - dungeon[-1][j])

        for i in range(m - 2, -1, -1):
            for j in range(n - 2, -1, -1):
                min_health[i][j] = max(
                    1,
                    min(
                        min_health[i + 1][j] - dungeon[i][j],
                        min_health[i][j + 1] - dungeon[i][j],
                    ),
                )

        return min_health[0][0]


# Time Complexity = O(N * M), Space Complexity = O(N * M)
