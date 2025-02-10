# Problem description here https://leetcode.com/problems/word-search/description/


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])

        def is_exist(r, c, index):
            if index == len(word):  # Found the word
                return True
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols  # Out of bounds
                or board[r][c] != word[index]  # Character mismatch
            ):
                return False

            temp, board[r][c] = board[r][c], "#"  # Mark as visited
            for dr, dc in [(0, 1), (0, -1), (1, 0), (-1, 0)]:  # Four directions
                if is_exist(r + dr, c + dc, index + 1):
                    return True
            board[r][c] = temp  # Backtrack

            return False

        for i in range(rows):
            for j in range(cols):
                if board[i][j] == word[0] and is_exist(i, j, 0):
                    return True

        return False


# Time Complexity = O(N * M * 4^L), Space Complexity = O(L)
# Where N and M are the number of rows and columns in board respectively
# and L is the length of the word

"""
# My original solution (same time and space complexity)
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        visited = set()

        def is_exist(idxx, idyy, lenw):
            visited.add((idxx, idyy))
            if lenw == len(word) - 1:
                return True
            dirc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in dirc:
                n_idxx, n_idyy = idxx + dr, idyy + dc
                if (
                    0 <= n_idxx <= len(board) - 1
                    and 0 <= n_idyy <= len(board[0]) - 1
                    and word[lenw + 1] == board[n_idxx][n_idyy]
                    and (n_idxx, n_idyy) not in visited
                ):
                    if is_exist(n_idxx, n_idyy, lenw + 1):
                        return True

            visited.remove((idxx, idyy))
            return False

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == word[0]:
                    if is_exist(i, j, 0):
                        return True

        return False
"""
