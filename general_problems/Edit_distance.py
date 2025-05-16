# Problem description here https://leetcode.com/problems/edit-distance/description/


class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        @cache
        def dp(i, j):
            if i == 0 or j == 0:
                return i + j
            if word1[i - 1] == word2[j - 1]:
                return dp(i - 1, j - 1)

            return (
                min(
                    dp(i, j - 1),  # Insert
                    dp(i - 1, j),  # Delete
                    dp(i - 1, j - 1),  # Replace
                )
                + 1
            )

        return dp(len(word1), len(word2))


# Time Complexity: O(M * N), Space Complexity: O(M * N)
# where M and N are the lengths of word1 and word2 respectively
